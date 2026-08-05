````markdown
# 🚀 AttendX – AI Powered Smart Attendance Management System

## 🌟 Overview

**AttendX** is an AI-powered attendance management platform designed to modernize classroom attendance through **Face Recognition**, **Voice Recognition**, and **QR Code-based classroom enrollment**.

The platform minimizes manual effort, reduces proxy attendance, and provides teachers with an intelligent dashboard to manage attendance efficiently while giving students a seamless attendance experience.

---

## 🎯 Key Highlights

- 🤖 AI-powered Face Recognition
- 🎤 Voice Recognition based Authentication
- 📱 QR Code Classroom Joining
- 🔐 Secure Password Authentication
- ☁️ Cloud Database using Supabase
- 👨‍🏫 Teacher Dashboard
- 👨‍🎓 Student Dashboard
- 📊 Attendance Analytics
- ⚡ Real-time Attendance Verification

---

## 🖥️ Live Demo

### 🌐 https://attend-x-landing-page-six.vercel.app/

Experience the complete application online.

---

## 🏗️ System Architecture

```text
                    Teacher Login
                          │
                          ▼
                 Create Classroom
                          │
                          ▼
                 Generate Join Code
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
   QR Code Join                 Student Registration
          │                               │
          └───────────────┬───────────────┘
                          ▼
              Face & Voice Enrollment
                          │
                          ▼
            AI Verification Pipeline
         (Face Recognition + Voice Match)
                          │
                          ▼
             Attendance Successfully Marked
                          │
                          ▼
                  Supabase Cloud Database
                          │
                          ▼
             Teacher & Student Dashboard
```

---

## 🧠 AI Technologies Used

### Face Recognition

- Face Detection
- Face Embedding Extraction
- SVM-based Classification
- Identity Verification

### Voice Recognition

- Voice Embeddings
- Speaker Verification
- Identity Authentication

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | Streamlit |
| Backend | Python |
| Database | Supabase |
| Computer Vision | OpenCV, Dlib, face_recognition |
| Voice Recognition | Resemblyzer |
| Machine Learning | Scikit-learn (SVM) |
| Authentication | bcrypt |

---

## 🔐 Security Features

- Encrypted Password Storage using bcrypt
- Secure Authentication
- Role-based Access
- Duplicate Attendance Prevention
- Cloud Database Security

---

## 💡 Why AttendX?

Traditional attendance systems are slow, manual, and vulnerable to proxy attendance.

AttendX leverages Artificial Intelligence to automate attendance using multiple authentication methods, making the process faster, more secure, and highly reliable.

---

## 🚀 Future Enhancements

- 📱 Mobile Application
- 📧 Email Notifications
- 📊 Advanced Attendance Analytics
- 🌍 Multi-Institution Support
- 🐳 Docker Deployment
- ☁️ CI/CD Integration
- 🔍 Face Liveness Detection
- 📄 PDF/Excel Attendance Reports

---

## 🎓 Learning Outcomes

This project helped me gain practical experience in:

- Full Stack Development
- Computer Vision
- Voice Recognition
- Machine Learning
- Authentication & Security
- Database Design
- Cloud Integration
- Software Architecture

---

## 👨‍💻 Developer

**Piyush Yadav**

GitHub: https://github.com/piyushkz960-ship-it

---

## ⭐ Support

If you found this project interesting, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
````
