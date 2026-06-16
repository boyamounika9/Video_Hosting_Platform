# 🎬 VidVault — Video Hoisting Platform

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2.30-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

**A full-stack video streaming web application built with Django, using local file storage and SQLite.**

[Features](#-features) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack) • [Setup](#-local-setup) • [Project Structure](#-project-structure)

</div>

---

## 📸 Overview

VidVault is a YouTube-inspired video hosting platform where users can register, upload videos with thumbnails, browse content on the homepage, and watch videos on a dedicated playback page. All media files are stored locally and the database uses **SQLite** for easier deployment and portability.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | Register, Login, Logout with Django's built-in auth system |
| 🎥 **Video Upload** | Upload MP4 videos with thumbnails directly to local storage |
| 🏠 **Homepage Feed** | Browse all uploaded videos in a card-grid layout |
| ▶️ **Video Playback** | Dedicated playback page with HTML5 video player |
| 👤 **User Profile** | View all videos uploaded by the logged-in user |
| 🔒 **Forgot Password** | Password reset functionality |
| 🗄️ **SQLite DB** | Default lightweight database for the platform |
| 🟢 **Health Check** | Dedicated `/health/` endpoint for monitoring and cron jobs |
| 🌙 **Dark UI** | Netflix-inspired dark theme with responsive design |
| 🖼️ **Favicon** | Custom VidVault play-button favicon |
| 🕐 **IST Timezone** | All timestamps shown in Indian Standard Time (IST) |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     User Browser                        │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Requests
                      ▼
┌─────────────────────────────────────────────────────────┐
│              Django Application (Python 3.9)            │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │ Auth /   │  │ Upload   │  │ Playback │  │Profile │  │
│  │ Register │  │ Videos   │  │ Videos   │  │  Page  │  │
│  └──────────┘  └────┬─────┘  └────┬─────┘  └────────┘  │
│                     │             │                      │
└─────────────────────┼─────────────┼──────────────────────┘
                      │             │
          ┌───────────▼──┐    ┌─────▼──────────┐
          │  Local FS    │    │  SQLite         │
          │  (Media)     │    │  (db.sqlite3)   │
          │  - videos/   │    │                 │
          │  - thumbnails│    │                 │
          └──────────────┘    └─────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Django 4.2.30** — Web framework
- **Python 3.9+** — Programming language
- **Pillow** — Image processing for thumbnails

### Database
- **SQLite3** — Lightweight, local relational database

### Storage
- **Local File System** (`media/`) — Local storage for videos and thumbnails

### Frontend
- **HTML5 / CSS3 / Vanilla JS** — No frameworks, hand-crafted UI
- **Google Fonts** — Typography
- **HTML5 Video Player** — Native video playback

---

## 📁 Project Structure

```
Video_Hosting_Platform/
├── .venv/                        # Python virtual environment
├── requirements.txt              # Python dependencies
├── README.md
└── project/                      # Django root
    ├── manage.py
    ├── static/
    │   ├── css/
    │   │   └── style.css         # Global dark-theme stylesheet
    │   └── favicon.png           # VidVault favicon
    ├── templates/                # Global HTML templates
    │   ├── base.html             # Base layout (header, footer)
    │   ├── home.html             # Homepage video feed
    │   ├── playback.html         # Video player page
    │   └── profile.html          # User profile page
    ├── project/                  # Django settings & URLs
    │   ├── settings.py
    │   └── urls.py
    ├── videoupload/              # Video upload app
    │   ├── models.py             # VideoData model
    │   ├── views.py
    │   └── urls.py
    ├── loginandregister/         # Auth app (login, register)
    ├── homepage/                 # Homepage feed app
    ├── profile_page/             # User profile app
    ├── videoplayback/            # Video playback app
    └── forgotpassword/           # Password reset app
```

---

## ⚙️ Local Setup

### Prerequisites

| Tool | Version | Download |
|---|---|---|
| Python | 3.9+ | [python.org](https://python.org/downloads) |
| Git | Latest | [git-scm.com](https://git-scm.com) |

---

### 🍎 macOS / Linux

```bash
# 1. Clone the repository
git clone https://github.com/boyamounika9/Video_Hosting_Platform.git
cd Video_Hosting_Platform

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations and start server
cd project
python manage.py migrate
python manage.py runserver
```

---

### 🪟 Windows (Command Prompt)

```cmd
:: 1. Clone the repository
git clone https://github.com/boyamounika9/Video_Hosting_Platform.git
cd Video_Hosting_Platform

:: 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

:: 3. Install dependencies
pip install -r requirements.txt

:: 4. Run migrations and start server
cd project
python manage.py migrate
python manage.py runserver
```

---

## 🗄️ Database Model

### `VideoData` (videoupload app)

| Field | Type | Description |
|---|---|---|
| `title` | `CharField(200)` | Video title |
| `description` | `TextField` | Video description |
| `video_file` | `FileField` | Stored locally at `videos/` |
| `thumbnail` | `ImageField` | Stored locally at `thumbnails/` |
| `upload_time` | `DateTimeField` | Auto-set on upload (IST) |
| `uploaded_by` | `ForeignKey(User)` | Linked to Django auth user |

---

## 🌐 URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `homepage` | Homepage video feed |
| `/upload/` | `VideoUpload` | Upload a new video |
| `/playback/<id>/` | `playback` | Watch a specific video |
| `/profile/` | `profile_page` | User's uploaded videos |
| `/login/` | `login` | User login |
| `/register/` | `register` | User registration |
| `/forgotpassword/` | `forgot_password` | Password reset |
| `/health/` | `health` | Health endpoint for cron jobs |
| `/admin/` | Django Admin | Admin panel |

---

## 🚀 Deployment Notes

- Set `DEBUG = False` in `settings.py` before deploying to production
- Add your domain to `ALLOWED_HOSTS`
- Set a strong, random `SECRET_KEY` via environment variable
- Use `python manage.py collectstatic` to collect static files
- Consider using **Gunicorn + Nginx** or **Render** for hosting

---

## 👥 Contributors

| Name | Role |
|---|---|
| Jeevan Kumar Guduru | Backend Developer |
| Mounika Boya | Project Owner |

---

## 📄 License

This project is for educational purposes. All rights reserved © 2026 VidVault Team.
