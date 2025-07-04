# 🔮 CryptoOracle

**CryptoOracle** is a full-stack crypto analytics dashboard developed by **Aaron of Warrior Tech Solutions**. It combines machine learning, market sentiment analysis, and real-time investment recommendations to empower traders, analysts, and enthusiasts with actionable insights.

---

## 🚀 Features

- ✅ Predictive price modeling via trained ML algorithms
- ✅ TextBlob-powered sentiment analysis on crypto trends
- ✅ Rule-based investment recommendations
- ✅ Interactive frontend dashboard (vanilla JS + HTML)
- ✅ FastAPI backend with Swagger UI (`/docs`)
- ✅ Clean deployment via Docker or startup script
- ✅ GitHub Pages support for instant hosting

---

## 🛠 Tech Stack

| Layer       | Tech                             |
|-------------|----------------------------------|
| Frontend    | HTML, CSS, JavaScript            |
| Backend     | FastAPI, Uvicorn                 |
| ML & NLP    | Pandas, Joblib, NLTK, TextBlob   |
| Deployment  | Docker / Render / GitHub Pages   |

---

## 🧪 Local Setup

### Backend

```bash
# Run locally with auto-reload
uvicorn backend.main:app --reload
