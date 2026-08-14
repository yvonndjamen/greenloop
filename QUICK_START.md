# ⚡ Quick Start - GreenLoop

Get **GreenLoop** running in 60 seconds!

## 🚀 Installation

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Application
```bash
python app.py
```

### Step 4: Open Browser
Visit: **http://localhost:5000**

---

## 🔐 Default Credentials

- **Username:** demo
- **Password:** demo123

---

## 📊 Test the Dashboard

1. Login successfully
2. See the KPI cards and metrics
3. Visit these URLs to simulate QR scans:
   - `http://localhost:5000/scan/PKG001?action=shipped`
   - `http://localhost:5000/scan/PKG002?action=returned`
   - `http://localhost:5000/scan/PKG999?action=shipped`
4. Refresh the dashboard to see updates

---

## ✨ What to Try

- Change your profile
- Add new packages via `/scan/` URLs
- Inspect `data/packages.json`
- Modify `static/style.css`
- Read and understand `app.py`

---

**Happy learning!**
