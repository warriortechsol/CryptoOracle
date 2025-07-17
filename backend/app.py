from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from backend.predictor import predict_price
from backend.sentiment import get_sentiment_score
from backend.recommender import get_recommendation

app = FastAPI()

# 🔐 CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 🛡️ Validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"[VALIDATION ERROR] {exc}")
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors()})
    )

# 🫀 Health check
@app.get("/")
async def root():
    return { "message": "CryptoOracle backend is online." }

# 🧪 Debug route to inspect files (optional)
@app.get("/debug/files")
async def debug_files():
    import os
    return {
        "models": os.listdir("models") if os.path.exists("models") else "models folder missing",
        "data": os.listdir("backend/data") if os.path.exists("backend/data") else "data folder missing"
    }

# 📦 Request models
class PredictionRequest(BaseModel):
    symbol: str
    current_price: float

class SentimentRequest(BaseModel):
    symbol: str

class RecommendationRequest(BaseModel):
    predicted_price: float
    current_price: float

# 🔮 Prediction route
@app.post("/predict")
async def predict_route(payload: PredictionRequest):
    try:
        print(f"[ROUTE] /predict received: {payload}")
        predicted = predict_price(payload.symbol, payload.current_price)
        sentiment_score = get_sentiment_score(payload.symbol)
        recommendation = get_recommendation(predicted, payload.current_price)

        return {
            "predicted_price": predicted,
            "sentiment_score": sentiment_score,
            "recommendation": recommendation
        }

    except Exception as e:
        print(f"[ERROR] /predict failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 📈 Sentiment route
@app.post("/sentiment")
async def sentiment_route(payload: SentimentRequest):
    try:
        print(f"[ROUTE] /sentiment received: {payload}")
        score = get_sentiment_score(payload.symbol)
        return { "sentiment_score": score }
    except Exception as e:
        print(f"[ERROR] /sentiment failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 🧭 Recommendation route
@app.post("/recommend")
async def recommend_route(payload: RecommendationRequest):
    try:
        print(f"[ROUTE] /recommend received: {payload}")
        advice = get_recommendation(payload.predicted_price, payload.current_price)
        return { "recommendation": advice }
    except Exception as e:
        print(f"[ERROR] /recommend failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

