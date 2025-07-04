#!/bin/bash

# Navigate to backend directory
cd backend

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Launch FastAPI app with Uvicorn
uvicorn main:app --host 0.0.0.0 --port $PORT
