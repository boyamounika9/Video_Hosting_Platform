## 🖥️ Windows Setup Guide

### **Step 1 — Prerequisites (install these first)**
- Install **Python 3.9+** → [python.org/downloads](https://python.org/downloads)  
  ✅ Check **"Add Python to PATH"** during install
- Install **Git** → [git-scm.com](https://git-scm.com)

---

### **Step 2 — Clone & Setup**
```cmd
git clone https://github.com/boyamounika9/Video_Hoisting_Platform.git
cd Video_Hoisting_Platform

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

### **Step 3 — Run the server**
```cmd
cd project
python manage.py migrate
python manage.py runserver
```
