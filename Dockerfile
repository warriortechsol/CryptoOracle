# 🐍 Base Python image
FROM python:3.10-slim

# 🔧 Install system-level dependencies for pandas/numpy/nltk
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    curl \
    wget \
    git

# 💼 Set working directory
WORKDIR /app

# 📦 Upgrade pip and install Python dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 🧠 Copy source code
COPY backend/ ./backend/ 

# 📚 Download NLTK corpora (optional but useful for sentiment analysis)
RUN python -m nltk.downloader vader_lexicon
RUN python -m nltk.downloader punkt

# 🚀 Run FastAPI app using Uvicorn
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8080"]


