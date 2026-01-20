import os
import uuid
from typing import List, Optional, Dict
try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None
try:
    from langchain_chroma import Chroma
except ImportError:
    try:
        from langchain_community.vectorstores import Chroma
    except ImportError:
        Chroma = None
try:
    from langchain_huggingface import HuggingFaceEmbeddings
except ImportError:
    from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class RAGChatbot:
    """
    RAG (Retrieval-Augmented Generation) Chatbot that can answer questions
    based on indexed documents.
    """
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Initialize the RAG chatbot.
        
        Args:
            persist_directory: Directory to persist the vector database
        """
        # Check for Groq API key
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables. "
                "Please set it in your .env file or environment."
            )
        
        # Initialize embeddings using HuggingFace (free, local)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Initialize LLM with Groq
        if ChatGroq is None:
            raise ValueError(
                "langchain-groq is not installed. Please install it with: pip install langchain-groq"
            )
        self.llm = ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0.7,
            groq_api_key=api_key
        )
        
        # Initialize vector store
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)
        
        # Create or load vector store
        try:
            self.vector_store = Chroma(
                persist_directory=persist_directory,
                embedding_function=self.embeddings,
            )
        except Exception as e:
            print(f"Warning: Could not initialize ChromaDB: {e}")
            print("Chatbot will work without document indexing (direct LLM mode)")
            self.vector_store = None
        
        # Initialize retrieval QA chain
        self.qa_chain = None
        self._update_qa_chain()
        
        # Store conversation history (simple in-memory storage)
        self.conversations: Dict[str, List] = {}
    
    def _update_qa_chain(self):
        """Update the QA chain with current vector store."""
        if self.vector_store is None:
            self.qa_chain = None
            return
            
        try:
            # Try to get collection count
            collection_count = self.vector_store._collection.count()
            if collection_count == 0:
                # No documents indexed yet
                self.qa_chain = None
                return
        except (AttributeError, Exception):
            # Collection might not exist or be accessible, set chain to None
            self.qa_chain = None
            return
        
        # Create prompt template
        prompt_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer based on the context, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {question}

Provide a helpful and accurate answer:"""
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create retrieval chain using modern LangChain approach
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        self.qa_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def index_documents(self, documents: List[str], metadatas: Optional[List[dict]] = None):
        """
        Index documents for retrieval.
        
        Args:
            documents: List of text documents to index
            metadatas: Optional list of metadata dictionaries for each document
        """
        if not documents:
            return
        
        if self.vector_store is None:
            raise ValueError("Vector store not initialized. ChromaDB dependencies may be missing.")
        
        # Create Document objects
        doc_objects = []
        for i, doc_text in enumerate(documents):
            metadata = metadatas[i] if metadatas and i < len(metadatas) else {}
            doc_objects.append(Document(page_content=doc_text, metadata=metadata))
        
        # Add to vector store
        self.vector_store.add_documents(doc_objects)
        self.vector_store.persist()
        
        # Update QA chain
        self._update_qa_chain()
    
    def chat(self, message: str, conversation_id: Optional[str] = None) -> Dict:
        """
        Chat with the RAG chatbot.
        
        Args:
            message: User's question
            conversation_id: Optional conversation ID for maintaining context
        
        Returns:
            Dictionary with:
            - answer: The chatbot's response
            - conversation_id: The conversation ID
            - sources: List of source documents (if available)
        """
        # Generate or use conversation ID
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
        
        # Initialize conversation history if needed
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        
        # Add user message to history
        self.conversations[conversation_id].append({"role": "user", "content": message})
        
        # Get response
        if self.qa_chain is None:
            # No documents indexed, use LLM directly
            response = self.llm.invoke(message)
            answer = response.content if hasattr(response, 'content') else str(response)
            sources = []
        else:
            # Use RAG chain
            try:
                answer = self.qa_chain.invoke(message)
                # Get sources
                if self.vector_store:
                    retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
                    docs = retriever.get_relevant_documents(message)
                    sources = [doc.page_content[:200] + "..." for doc in docs]
                else:
                    sources = []
            except Exception as e:
                # Fallback to direct LLM
                response = self.llm.invoke(message)
                answer = response.content if hasattr(response, 'content') else str(response)
                sources = []
        
        # Add assistant response to history
        self.conversations[conversation_id].append({"role": "assistant", "content": answer})
        
        return {
            "answer": answer,
            "conversation_id": conversation_id,
            "sources": sources
        }
    
    def get_conversation_history(self, conversation_id: str) -> List[Dict]:
        """Get conversation history for a given conversation ID."""
        return self.conversations.get(conversation_id, [])
