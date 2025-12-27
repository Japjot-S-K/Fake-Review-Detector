# 🕵️ ReviewGuard — Fake Review Intelligence Platform

ReviewGuard is a full-stack web application that detects **suspicious product reviews** using **Natural Language Processing (NLP)**.
It provides **credibility scoring, explainable analysis, and a free review-rewriting assistant**, all deployed in production.

This project is built to demonstrate **real-world full-stack development**, not just model accuracy.

---

## 🌐 Live Demo

- **Backend API (Render)**  
  https://fake-review-detector-f0wz.onrender.com

- **Frontend (Vercel)**  
  (Add your Vercel deployment URL here)

---

## ✨ Key Features

### 🔍 Fake Review Detection
- Analyzes reviews for:
  - Language repetition
  - Sentiment imbalance
  - Low-information / generic content
- Generates a **Credibility Score (0–100)**
- Flags reviews as **Genuine** or **Suspicious**

---

### 🧠 Explainable Analysis (Explainable AI)
Instead of a black-box decision, the system explains **why** a review was flagged.

Example:
```
Why this review looks suspicious:
• Repeated or low-diversity language detected
• Overly positive sentiment detected
• Review is too short and lacks detail
```

---

### ✍️ Make Review Genuine (Free NLP Rewrite)
A **free, rule-based NLP rewrite engine** that:
- Removes spammy phrases
- Normalizes extreme sentiment
- Expands very short reviews
- Produces neutral, natural-sounding feedback

No paid APIs are used. This feature is fully offline and ethical, designed purely for demonstration.

---

### 🎨 Modern UI
- Dark SaaS-style interface
- Multi-section navigation
- Credibility meter
- Clean, responsive layout

---

## 🏗️ Architecture

```
Frontend (HTML / CSS / JS) → Vercel
        |
        | HTTPS REST API
        ↓
Backend (Flask + NLP) → Render
```

The frontend automatically switches between **local** and **production** APIs.

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript

### Backend
- Python
- Flask
- TextBlob (NLP)
- Regular Expressions
- Gunicorn

### Deployment
- **Vercel** — Frontend
- **Render** — Backend API

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs at:
```
http://127.0.0.1:5000
```

### 3️⃣ Frontend Setup
Open:
```
frontend/index.html
```

---

## 📡 API Endpoints

### Analyze Review
```
POST /analyze
```

Request:
```json
{
  "review": "Amazing amazing best product ever buy now"
}
```

Response:
```json
{
  "credibility_score": 32,
  "is_suspicious": true,
  "repetition_score": 40,
  "sentiment_score": 90,
  "reasons": [
    "Repeated or low-diversity language detected",
    "Overly positive sentiment detected",
    "Review is too short and lacks detail"
  ]
}
```

---

### Rewrite Review
```
POST /rewrite
```

Request:
```json
{
  "review": "Amazing amazing best ever buy now"
}
```

Response:
```json
{
  "rewritten_review": "The product works as expected and provides good value for its price. The quality appears reasonable and delivery was on time."
}
```

---

## 🚀 Why This Project Matters

This project demonstrates:
- Full-stack development
- REST API design
- NLP-based text analysis
- Explainable AI concepts
- Production deployment
- Frontend–backend integration
- Real-world debugging experience

---

## 📌 Future Improvements

- Review history & analytics dashboard
- Rewrite confidence score
- Before/after diff visualization
- User authentication
- Database integration
- ML-based classifier (Logistic Regression / BERT)
- Chrome extension

---

## 👤 Author

**Japjot Singh Kashyap**  
GitHub: https://github.com/YOUR_USERNAME

---

## 📄 License
This project is for educational and demonstration purposes.
