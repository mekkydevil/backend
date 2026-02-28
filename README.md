# 🎓 BNU Student Portal

A comprehensive full-stack student portal application with complete backend API, authentication, course management, payment processing, and AI chatbot.

## ⚠️ IMPORTANT: Two Servers Required

This application requires **BOTH** frontend and backend to be running simultaneously:
- **Frontend**: React app on port 5173
- **Backend**: FastAPI server on port 8001

**See [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md) for complete setup guide!**

---

## ✨ Features

### Student Features
- 🔐 **Authentication** - Secure login/register system
- 👤 **Profile Management** - View and update student information
- 📚 **Course Registration** - Browse and register for courses
- 📊 **Grade Tracking** - View grades and GPA by semester
- 💰 **Payment System** - Calculate tuition with GPA-based discounts
- 📝 **Quiz System** - Take quizzes with auto-grading
- 🤖 **AI Chatbot** - RAG-powered assistant for student queries
- 📱 **Responsive Design** - Works on all devices
- 🌐 **Bilingual** - Arabic/English support

### Admin Features
- 📈 **Dashboard** - System statistics and analytics
- 👥 **User Management** - Manage students and accounts
- 📋 **Course Management** - Add/edit courses
- 💳 **Payment Tracking** - Monitor payment status

---

## 🛠️ Tech Stack

### Frontend
- React 19 + Vite
- TailwindCSS
- React Router
- i18next (Internationalization)
- Formik (Forms)
- Lucide Icons

### Backend
- FastAPI (Python)
- Pydantic (Data Validation)
- JSON Database
- Groq API (LLM)
- ChromaDB (Vector Store)
- Uvicorn (ASGI Server)

---

## 🚀 Quick Start

### Prerequisites

- ✅ **Node.js** 16+ - [Download](https://nodejs.org/)
- ✅ **Python** 3.8+ - [Download](https://www.python.org/)
- ✅ **Groq API Key** - [Get free key](https://console.groq.com/)

### Installation

**📖 For detailed setup instructions, see [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)**

#### 1. Clone Repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

#### 2. Install Dependencies
```bash
# Frontend
npm install

# Backend
cd backend
pip install -r requirements.txt
```

#### 3. Create Database
```bash
cd backend
python seed_data.py
```

#### 4. Configure Environment
```bash
# Backend: Create backend/.env
GROQ_API_KEY=your_groq_api_key_here

# Frontend: .env already configured
VITE_API_BASE_URL=http://localhost:8001
```

#### 5. Start Servers (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd backend
python full_api.py
```
Backend runs on: `http://localhost:8001`

**Terminal 2 - Frontend:**
```bash
npm run dev
```
Frontend runs on: `http://localhost:5173`

---

## 🔑 Test Accounts

| Username | Password | Role    |
|----------|----------|---------|
| 1000001  | pass123  | Student |
| 2358858  | abcdef   | Student |
| admin    | admin123 | Admin   |

---

## 📡 API Endpoints

### Authentication
```
POST   /login                          - Login user
POST   /forgot-password                - Password reset
POST   /register                       - Register new user
```

### Student
```
GET    /api/student/{id}               - Get profile
GET    /api/student/{id}/grades        - Get grades & GPA
GET    /api/student/{id}/stats         - Get statistics
```

### Courses
```
GET    /api/courses                    - List courses
POST   /api/courses/register           - Register course
GET    /api/student/{id}/registrations - View registrations
```

### Payments
```
POST   /api/payment/calculate          - Calculate tuition
POST   /api/payment/process            - Process payment
```

### Quizzes
```
GET    /api/quizzes                    - List quizzes
POST   /api/quizzes/{id}/submit        - Submit answers
```

**Full API docs**: http://localhost:8001/docs (when backend is running)

---

## 📁 Project Structure

```
.
├── backend/                    # Backend API (FastAPI)
│   ├── full_api.py            # Main API server ⭐ RUN THIS
│   ├── database.py            # Database handler
│   ├── models.py              # Data models
│   ├── seed_data.py           # Create sample data
│   ├── rag_chatbot.py         # AI chatbot
│   ├── gpa_calculator.py      # GPA logic
│   └── requirements.txt       # Python dependencies
├── Data/
│   └── db.json                # JSON database
├── src/                       # Frontend (React)
│   ├── pages/                 # Page components
│   ├── services/              # API service layer
│   │   ├── authService.js     # Authentication
│   │   ├── studentService.js  # Student data
│   │   ├── courseService.js   # Course management
│   │   ├── paymentService.js  # Payments
│   │   └── chatService.js     # Chatbot
│   ├── config/
│   │   └── api.js            # API configuration
│   └── components/            # React components
├── public/                    # Static assets
├── .env                       # Frontend environment
├── package.json               # Node dependencies
├── SETUP_INSTRUCTIONS.md      # 📖 Detailed setup guide
├── FULL_BACKEND_GUIDE.md      # Complete API docs
└── README.md                  # This file
```

---

## 🧪 Testing

### Test Backend Health
```bash
curl http://localhost:8001/api/health
```

### Test API Endpoints
Open `test-api.html` in browser for interactive testing.

### Test Login
1. Go to http://localhost:5173
2. Login: `1000001` / `pass123`
3. Should redirect to dashboard

---

## 📜 Available Scripts

### Frontend
```bash
npm run dev      # Start development server (port 5173)
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Run ESLint
```

### Backend
```bash
python full_api.py          # Start complete API server (port 8001)
python seed_data.py         # Create/reset database
python test_chatbot.py      # Test chatbot
```

---

## 🔗 How It Works

```
┌──────────────────────────────────────────────────────────┐
│  Browser: http://localhost:5173                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  Frontend (React)                              │     │
│  │  - Login, Dashboard, Courses, Grades, etc.     │     │
│  └────────────────────────────────────────────────┘     │
│                       │                                   │
│                       │ HTTP Requests (fetch)             │
│                       ▼                                   │
└──────────────────────────────────────────────────────────┘
                        │
                        │ CORS Enabled ✅
                        ▼
┌──────────────────────────────────────────────────────────┐
│  Backend: http://localhost:8001                          │
│  ┌────────────────────────────────────────────────┐     │
│  │  FastAPI Server (40+ endpoints)                │     │
│  │  - Authentication, Courses, Grades, Payments   │     │
│  └────────────────────────────────────────────────┘     │
│                       │                                   │
│                       ▼                                   │
│  ┌────────────────────────────────────────────────┐     │
│  │  Data/db.json (Database)                       │     │
│  └────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────┘
```

**Both servers must run simultaneously!**

---

## 🐛 Troubleshooting

### "Failed to fetch" Error
**Problem**: Backend not running  
**Solution**: Start backend with `cd backend && python full_api.py`

### "Module not found" (Python)
**Problem**: Missing dependencies  
**Solution**: `cd backend && pip install -r requirements.txt`

### "Cannot find module" (Node)
**Problem**: Missing packages  
**Solution**: `npm install`

### "Database not found"
**Problem**: `Data/db.json` missing  
**Solution**: `cd backend && python seed_data.py`

### Port Already in Use
**Problem**: Port 8001 or 5173 occupied  
**Solution**: Kill the process or use different port

### Login Not Working
**Problem**: Wrong credentials or backend not running  
**Solution**: Use `1000001` / `pass123` and verify backend is running

**More help**: See [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)

---

## 📚 Documentation

- **[SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)** - Complete setup guide
- **[FULL_BACKEND_GUIDE.md](./FULL_BACKEND_GUIDE.md)** - API documentation
- **[HOW_TO_USE_API.md](./HOW_TO_USE_API.md)** - API usage examples
- **[FRONTEND_BACKEND_CONNECTION.md](./FRONTEND_BACKEND_CONNECTION.md)** - Architecture
- **[COMPLETE_INTEGRATION_SUMMARY.md](./COMPLETE_INTEGRATION_SUMMARY.md)** - Integration overview

---

## 🎯 Key Features Explained

### GPA-Based Payment Discounts
- GPA ≥ 3.9: 25% discount
- GPA ≥ 3.7: 15% discount
- GPA ≥ 3.5: 10% discount

### Auto-Grading Quizzes
- Multiple choice questions
- Instant results
- Pass/fail based on 60% threshold

### RAG Chatbot
- Context-aware responses
- Conversation history
- Arabic/English support

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Commit: `git commit -m 'Add feature'`
5. Push: `git push origin feature-name`
6. Submit pull request

---

## 📄 License

This project is for educational purposes.

---

## 💡 For Developers

### Adding New API Endpoint

1. **Backend**: Add endpoint in `backend/full_api.py`
2. **Service**: Add function in `src/services/`
3. **Config**: Add endpoint in `src/config/api.js`
4. **Frontend**: Use service in your component

Example:
```javascript
// 1. Add to src/config/api.js
newEndpoint: `${API_BASE_URL}/api/new-endpoint`

// 2. Add to src/services/newService.js
export const callNewEndpoint = async () => {
  const response = await fetch(API_ENDPOINTS.newEndpoint);
  return await response.json();
};

// 3. Use in component
import { callNewEndpoint } from '../services/newService';
const data = await callNewEndpoint();
```

---

## 🆘 Support

**Before asking for help, please:**
1. ✅ Read [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)
2. ✅ Check both servers are running
3. ✅ Try test credentials: `1000001` / `pass123`
4. ✅ Open `test-api.html` to test backend
5. ✅ Check browser console for errors (F12)

**Still stuck?**
- Check API docs: http://localhost:8001/docs
- Review documentation files listed above
- Open an issue on GitHub

---

## ⚡ Quick Reference

| What | Where | Port |
|------|-------|------|
| Frontend | http://localhost:5173 | 5173 |
| Backend | http://localhost:8001 | 8001 |
| API Docs | http://localhost:8001/docs | 8001 |
| Database | Data/db.json | - |
| Test Page | test-api.html | - |

**Start Command:**
```bash
# Terminal 1
cd backend && python full_api.py

# Terminal 2  
npm run dev
```

---

## 🎉 Success Checklist

You're all set if you can:
- ✅ Access http://localhost:5173 (login page)
- ✅ Access http://localhost:8001/api/health (shows "healthy")
- ✅ Login with `1000001` / `pass123`
- ✅ See student dashboard
- ✅ Navigate to different pages

**Congratulations! The system is fully integrated and working!** 🚀
