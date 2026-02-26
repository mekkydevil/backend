# BNU Student Portal

A comprehensive student portal application with integrated chatbot, GPA calculator, and campus map features.

## Features

- 🤖 **AI Chatbot** - RAG-powered assistant using Groq API
- 📊 **GPA Calculator** - Calculate term and accumulative GPA
- 🗺️ **Campus Map** - Interactive map with routing
- 🔐 **Authentication** - Secure login system
- 📱 **Responsive Design** - Works on all devices

## Tech Stack

### Frontend
- React 19
- Vite
- TailwindCSS
- React Router
- Leaflet (Maps)
- Lucide Icons

### Backend
- FastAPI
- Python 3.11+
- Groq API (LLM)
- ChromaDB (Vector Store)

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Groq API key ([Get one here](https://console.groq.com/))

### Option 1: Automated Setup (Windows)

```powershell
# Start both frontend and backend
.\start-dev.ps1
```

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# Start server
python main.py
```

Backend runs on: `http://localhost:8000`

#### Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs on: `http://localhost:5173`

## Environment Configuration

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:8000
```

### Backend (backend/.env)
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
.
├── backend/                 # FastAPI backend
│   ├── main.py             # Main API server
│   ├── rag_chatbot.py      # Chatbot implementation
│   ├── gpa_calculator.py   # GPA calculation logic
│   └── requirements.txt    # Python dependencies
├── src/                    # React frontend
│   ├── components/         # React components
│   ├── pages/             # Page components
│   ├── services/          # API service layer
│   ├── config/            # Configuration files
│   └── css/               # Stylesheets
├── public/                # Static assets
└── INTEGRATION_GUIDE.md   # Detailed integration docs
```

## Available Scripts

### Frontend
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

### Backend
```bash
python main.py              # Start FastAPI server
python test_chatbot.py      # Test chatbot functionality
```

## Integration Details

The frontend communicates with the backend through a service layer:

- **Chat Service** (`src/services/chatService.js`) - Handles chatbot interactions
- **GPA Service** (`src/services/gpaService.js`) - Manages GPA calculations
- **API Config** (`src/config/api.js`) - Centralized API endpoint configuration

See [INTEGRATION_GUIDE.md](./INTEGRATION_GUIDE.md) for detailed integration documentation.

## Features Overview

### Chatbot
- Natural language conversations in Arabic/English
- Context-aware responses
- Conversation history
- Voice input support

### GPA Calculator
- Term GPA calculation
- Accumulative GPA tracking
- Multiple subjects support
- Grade conversion (score to letter grade)

### Campus Map
- Interactive map with OpenStreetMap
- Location search with autocomplete
- Route planning
- Distance and time estimates

## Troubleshooting

### Backend Issues
- Ensure Python 3.11+ is installed
- Check GROQ_API_KEY is set correctly
- Verify port 8000 is not in use

### Frontend Issues
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Check backend is running on port 8000
- Verify VITE_API_BASE_URL in .env

### CORS Errors
- Backend has CORS middleware configured
- Vite proxy is set up for /api routes
- Check both servers are running

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes.

## Support

For issues and questions, please check:
- [INTEGRATION_GUIDE.md](./INTEGRATION_GUIDE.md) - Integration documentation
- Backend API docs at http://localhost:8000/docs
- Project issues on GitHub
