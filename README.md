# 🎬 StreamVids — Cloud-Native Video Streaming Platform

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2.30-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-Media_Storage-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)
![AWS RDS](https://img.shields.io/badge/AWS_RDS-Aurora_MySQL-527FFF?style=for-the-badge&logo=amazonrds&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**A full-stack video streaming web application built with Django, backed by AWS cloud services for scalable media storage and database management.**

[Features](#-features) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack) • [Setup](#-local-setup) • [AWS Config](#-aws-configuration) • [Project Structure](#-project-structure)

</div>

---

## 📸 Overview

StreamVids is a YouTube-inspired video streaming platform where users can register, upload videos with thumbnails, browse content on the homepage, and watch videos on a dedicated playback page. All media files are stored on **AWS S3** and the database is hosted on **AWS Aurora (MySQL)** via **RDS**, making it production-ready and cloud-native.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | Register, Login, Logout with Django's built-in auth system |
| 🎥 **Video Upload** | Upload MP4 videos with thumbnails directly to AWS S3 |
| 🏠 **Homepage Feed** | Browse all uploaded videos in a card-grid layout |
| ▶️ **Video Playback** | Dedicated playback page with HTML5 video player |
| 👤 **User Profile** | View all videos uploaded by the logged-in user |
| 🔒 **Forgot Password** | Password reset functionality |
| ☁️ **AWS S3 Storage** | All media (videos & thumbnails) served from S3 |
| 🗄️ **AWS RDS** | Aurora MySQL cluster for cloud-hosted database |
| 🔑 **Secrets Manager** | DB credentials fetched securely via AWS Secrets Manager |
| 🌙 **Dark UI** | Netflix-inspired dark theme with responsive design |
| 🖼️ **Favicon** | Custom StreamVids play-button favicon |
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
          │  AWS S3      │    │  AWS RDS        │
          │  (Media)     │    │  Aurora MySQL   │
          │  - videos/   │    │  (streamvids DB)│
          │  - thumbnails│    │                 │
          └──────────────┘    └────────┬────────┘
                                       │
                              ┌────────▼────────┐
                              │  AWS Secrets    │
                              │  Manager        │
                              │  (DB Password)  │
                              └─────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Django 4.2.30** — Web framework
- **Python 3.9+** — Programming language
- **mysqlclient** — MySQL database adapter
- **boto3** — AWS SDK for Python
- **django-storages** — S3 file storage backend
- **Pillow** — Image processing for thumbnails

### Database
- **AWS Aurora MySQL** (RDS cluster) — Cloud-hosted relational database
- **AWS Secrets Manager** — Secure credential management for DB passwords

### Storage
- **AWS S3** (`streamvids-media`) — Object storage for videos and thumbnails

### Frontend
- **HTML5 / CSS3 / Vanilla JS** — No frameworks, hand-crafted UI
- **Google Fonts** — Typography
- **HTML5 Video Player** — Native video playback

---

## 📁 Project Structure

```
Video_Streaming_Platform/
├── .venv/                        # Python virtual environment
├── requirements.txt              # Python dependencies
├── README.md
└── project/                      # Django root
    ├── manage.py
    ├── .env                      # ⚠️ Local secrets (not committed)
    ├── static/
    │   ├── css/
    │   │   └── style.css         # Global dark-theme stylesheet
    │   └── favicon.png           # StreamVids favicon
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
| MySQL Client | 8.0+ | [dev.mysql.com](https://dev.mysql.com/downloads/installer) |
| AWS CLI | Latest | [aws.amazon.com/cli](https://aws.amazon.com/cli/) |

---

### 🍎 macOS / Linux

```bash
# 1. Clone the repository
git clone https://github.com/boyamounika9/Video_Streaming_Platform.git
cd Video_Streaming_Platform

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file inside project/ folder
cat > project/.env << EOF
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_STORAGE_BUCKET_NAME=streamvids-media
AWS_S3_REGION_NAME=ap-south-1
EOF

# 5. Configure AWS CLI
aws configure

# 6. Run migrations and start server
cd project
export $(cat .env | xargs) && python manage.py migrate
export $(cat .env | xargs) && python manage.py runserver
```

---

### 🪟 Windows (Command Prompt)

```cmd
:: 1. Clone the repository
git clone https://github.com/boyamounika9/Video_Streaming_Platform.git
cd Video_Streaming_Platform

:: 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

:: 3. Install dependencies
pip install -r requirements.txt

:: 4. Create .env file inside project\ folder (or create manually)
::    File: project\.env
::    Content:
::    AWS_ACCESS_KEY_ID=your_access_key_id
::    AWS_SECRET_ACCESS_KEY=your_secret_access_key
::    AWS_STORAGE_BUCKET_NAME=streamvids-media
::    AWS_S3_REGION_NAME=ap-south-1

:: 5. Configure AWS CLI
aws configure

:: 6. Set environment variables and run
cd project
set AWS_ACCESS_KEY_ID=your_access_key_id
set AWS_SECRET_ACCESS_KEY=your_secret_access_key
set AWS_STORAGE_BUCKET_NAME=streamvids-media
set AWS_S3_REGION_NAME=ap-south-1
python manage.py migrate
python manage.py runserver
```

> ⚠️ **Windows note:** If `mysqlclient` fails to install, run:
> ```cmd
> pip install mysqlclient --only-binary=mysqlclient
> ```

---

## ☁️ AWS Configuration

### Required AWS Services

| Service | Purpose | Details |
|---|---|---|
| **IAM** | Access control | Create an IAM user with `AmazonS3FullAccess` + `SecretsManagerReadWrite` |
| **RDS Aurora MySQL** | Database | Cluster endpoint, port 3306, DB name: `streamvids` |
| **Secrets Manager** | DB credentials | Auto-created with RDS cluster, stores `username` + `password` |
| **S3** | Media storage | Bucket: `streamvids-media`, Region: `ap-south-1`, Public read policy |

### S3 Bucket Policy (Public Read)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::streamvids-media/*"
        }
    ]
}
```

### RDS Security Group

Make sure your **RDS Security Group** has an inbound rule:

| Type | Protocol | Port | Source |
|---|---|---|---|
| MySQL/Aurora | TCP | 3306 | Your IP address |

---

## 🗄️ Database Model

### `VideoData` (videoupload app)

| Field | Type | Description |
|---|---|---|
| `title` | `CharField(200)` | Video title |
| `description` | `TextField` | Video description |
| `video_file` | `FileField` | Stored in S3 at `videos/` |
| `thumbnail` | `ImageField` | Stored in S3 at `thumbnails/` |
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
| `/admin/` | Django Admin | Admin panel |

---

## 🔐 Environment Variables

Create a `.env` file in the `project/` directory:

```env
AWS_ACCESS_KEY_ID=your_iam_access_key
AWS_SECRET_ACCESS_KEY=your_iam_secret_key
AWS_STORAGE_BUCKET_NAME=streamvids-media
AWS_S3_REGION_NAME=ap-south-1
```

> 🔒 **Never commit this file to Git.** It is already listed in `.gitignore`.

---

## 🚀 Deployment Notes

- Set `DEBUG = False` in `settings.py` before deploying to production
- Add your domain to `ALLOWED_HOSTS`
- Set a strong, random `SECRET_KEY` via environment variable
- Use `python manage.py collectstatic` to collect static files
- Consider using **Gunicorn + Nginx** or **AWS Elastic Beanstalk** for hosting

---

## 👥 Contributors

| Name | Role |
|---|---|
| Jeevan Kumar Guduru | Backend Developer |
| Mounika Boya | Project Owner |

---

## 📄 License

This project is for educational purposes. All rights reserved © 2026 StreamVids Team.