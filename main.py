from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv

from gpa_calculator import calculate_gpa, GPACourse
from rag_chatbot import RAGChatbot

load_dotenv()

app = FastAPI(title="GPA Calculator & RAG Chatbot API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG chatbot
rag_chatbot = None

@app.on_event("startup")
async def startup_event():
    global rag_chatbot
    try:
        rag_chatbot = RAGChatbot()
        print("RAG Chatbot initialized successfully")
    except Exception as e:
        print(f"Warning: RAG Chatbot initialization failed: {e}")
        print("Chatbot endpoints will not be available")


# ==================== GPA Calculator Endpoints ====================

class CourseInput(BaseModel):
    name: str = Field(..., description="Course name")
    credits: float = Field(..., gt=0, description="Number of credits")
    grade: str = Field(..., description="Letter grade (A, B, C, D, F)")

class GPARequest(BaseModel):
    courses: List[CourseInput] = Field(..., description="List of courses")

class GPAResponse(BaseModel):
    gpa: float = Field(..., description="Calculated GPA")
    total_credits: float = Field(..., description="Total credits")
    total_points: float = Field(..., description="Total grade points")

@app.post("/api/gpa/calculate", response_model=GPAResponse)
async def calculate_gpa_endpoint(request: GPARequest):
    """
    Calculate GPA from a list of courses.
    
    Grade scale:
    - A: 4.0
    - B: 3.0
    - C: 2.0
    - D: 1.0
    - F: 0.0
    """
    try:
        courses = [GPACourse(name=course.name, credits=course.credits, grade=course.grade.upper()) 
                  for course in request.courses]
        result = calculate_gpa(courses)
        return GPAResponse(
            gpa=result["gpa"],
            total_credits=result["total_credits"],
            total_points=result["total_points"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# ==================== RAG Chatbot Endpoints ====================

class ChatRequest(BaseModel):
    message: str = Field(..., description="User's question")
    conversation_id: Optional[str] = Field(None, description="Optional conversation ID for context")

class ChatResponse(BaseModel):
    response: str = Field(..., description="Chatbot's response")
    conversation_id: str = Field(..., description="Conversation ID")
    sources: Optional[List[str]] = Field(None, description="Source documents used")

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat with the RAG-powered chatbot.
    The chatbot can answer questions based on indexed documents.
    """
    if rag_chatbot is None:
        raise HTTPException(
            status_code=503, 
            detail="RAG Chatbot is not initialized. Please check your Groq API key and configuration."
        )
    
    try:
        response = rag_chatbot.chat(request.message, request.conversation_id)
        return ChatResponse(
            response=response["answer"],
            conversation_id=response["conversation_id"],
            sources=response.get("sources", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@app.post("/api/chat/index-documents")
async def index_documents(documents: List[str]):
    """
    Index documents for the RAG system.
    Pass a list of text documents to be indexed and searchable.
    
    Note: Document indexing requires ChromaDB to be fully installed.
    If you get an error, the chatbot will still work in direct LLM mode.
    """
    if rag_chatbot is None:
        raise HTTPException(
            status_code=503, 
            detail="RAG Chatbot is not initialized. Please check your Groq API key and configuration."
        )
    
    try:
        rag_chatbot.index_documents(documents)
        return {"message": f"Successfully indexed {len(documents)} documents"}
    except ValueError as e:
        # Vector store not initialized
        raise HTTPException(
            status_code=503,
            detail=f"Document indexing is not available: {str(e)}. The chatbot is working in direct LLM mode (without document retrieval). To enable document indexing, ChromaDB dependencies need to be fully installed."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indexing documents: {str(e)}")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "rag_chatbot_available": rag_chatbot is not None
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
