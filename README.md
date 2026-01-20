# Backend API - GPA Calculator & RAG Chatbot

A FastAPI backend that provides two main features:
- **GPA Calculator**: Calculate GPA from course grades and credits
- **RAG Chatbot**: AI-powered chatbot using Retrieval-Augmented Generation

## Features

### GPA Calculator
- Calculate GPA from multiple courses
- Supports standard letter grades (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F)
- Returns GPA, total credits, and total points

### RAG Chatbot
- Powered by Groq API (Llama 3.1)
- Document indexing with ChromaDB
- Conversation history support
- Context-aware responses

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create `.env` file:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Start the server:**
   ```powershell
   .\start_server.ps1
   ```

   Or manually:
   ```bash
   python main.py
   ```

## API Endpoints

### Health Check
- **GET** `/api/health` - Check server status

### GPA Calculator
- **POST** `/api/gpa/calculate` - Calculate GPA
  ```json
  {
    "courses": [
      {"name": "Math", "credits": 3.0, "grade": "A"},
      {"name": "English", "credits": 4.0, "grade": "B+"}
    ]
  }
  ```

### Chat
- **POST** `/api/chat` - Chat with the RAG chatbot
  ```json
  {
    "message": "What is machine learning?",
    "conversation_id": "optional-conversation-id"
  }
  ```

- **POST** `/api/chat/index-documents` - Index documents for RAG
  ```json
  ["Document 1 text", "Document 2 text"]
  ```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing

Run the test scripts:
```powershell
# Test chat API
.\test_chat.ps1 -Question "What is machine learning?"

# Test full suite
python test_chat_api.py
```

## Requirements

- Python 3.8+
- FastAPI
- Groq API key
- See `requirements.txt` for full dependencies
