## 🖥️ Windows Setup Guide

### **Step 1 — Prerequisites (install these first)**
- Install **Python 3.9+** → [python.org/downloads](https://python.org/downloads)  
  ✅ Check **"Add Python to PATH"** during install
- Install **Git** → [git-scm.com](https://git-scm.com)
- Install **MySQL client** (needed for `mysqlclient`):
  - Download **MySQL Installer** → [dev.mysql.com/downloads/installer](https://dev.mysql.com/downloads/installer)
  - Install **MySQL Connector/C** only (not the full server)

---

### **Step 2 — Clone & Setup**
```cmd
git clone https://github.com/boyamounika9/Video_Streaming_Platform.git
cd Video_Streaming_Platform

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

### **Step 3 — Create `.env` file**
Inside the `project/` folder, create a file named `.env` with:
```
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=streamvids-media
AWS_S3_REGION_NAME=ap-south-1
```

---

### **Step 4 — Configure AWS CLI**
```cmd
pip install awscli
aws configure
```
Enter the same Access Key, Secret Key, region `ap-south-1`, format `json`

---

### **Step 5 — Run the server**
```cmd
cd project
set AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
set AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
set AWS_STORAGE_BUCKET_NAME=streamvids-media
set AWS_S3_REGION_NAME=ap-south-1
python manage.py migrate
python manage.py runserver
```

---

> ⚠️ **If `mysqlclient` install fails on Windows**, run:
> ```cmd
> pip install mysqlclient --only-binary=mysqlclient
> ```
> Or download the `.whl` from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
