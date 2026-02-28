# ⚠️ IMPORTANT: READ THIS FIRST!

## 🚨 This Project Requires TWO Servers to Run!

If someone told you "the backend is not working," it's because they need to **START THE BACKEND SERVER**!

---

## ✅ Quick Setup (3 Steps)

### Step 1: Install Dependencies
```bash
# Install frontend packages
npm install

# Install backend packages
cd backend
pip install -r requirements.txt
```

### Step 2: Create Database
```bash
# Still in backend folder
python seed_data.py
```

### Step 3: Start BOTH Servers

**Open TWO terminal windows:**

**Terminal 1 - Backend:**
```bash
cd backend
python full_api.py
```
✅ Should show: `Uvicorn running on http://0.0.0.0:8001`

**Terminal 2 - Frontend:**
```bash
npm run dev
```
✅ Should show: `Local: http://localhost:5173/`

---

## 🧪 Test It Works

1. Open browser: http://localhost:5173
2. Login with:
   - Username: `1000001`
   - Password: `pass123`
3. Should see student dashboard ✅

---

## 🆘 Still Not Working?

See **[SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)** for detailed help!

---

## 📋 What You Need Installed

- ✅ Node.js (v16+)
- ✅ Python (v3.8+)

Check versions:
```bash
node --version
python --version
```

---

## 🎯 The Problem Explained

This is a **full-stack application**:

```
Frontend (React)  →  Runs on port 5173
Backend (Python)  →  Runs on port 8001
```

**Both must be running at the same time!**

If you only run `npm run dev`, you'll get:
- ❌ Login fails
- ❌ "Failed to fetch" errors
- ❌ Nothing works

**Solution**: Run BOTH servers (see Step 3 above)

---

## 📚 More Documentation

- **[SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)** - Complete setup guide
- **[README.md](./README.md)** - Project overview
- **[FULL_BACKEND_GUIDE.md](./FULL_BACKEND_GUIDE.md)** - API documentation

---

## 💡 Pro Tip

Use `test-api.html` to test if backend is working:
1. Make sure backend is running
2. Open `test-api.html` in browser
3. Click "فحص الخادم" (Health Check)
4. Should show green success ✅

---

**TL;DR**: Run `python full_api.py` in backend folder, then `npm run dev` in root. Both must run together!
