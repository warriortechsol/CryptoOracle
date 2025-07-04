from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.predictor import predict_price
from backend.sentiment import get_sentiment_score
from backend.recommender import get_recommendation

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request models
class PredictionRequest(BaseModel):
    symbol: str
    current_price: float

class SentimentRequest(BaseModel):
    symbol: str

class RecommendationRequest(BaseModel):
    predicted_price: float
    current_price: float

# ✅ /predict
@app.post("/predict")
def predict_route(payload: PredictionRequest):
    try:
        predicted = predict_price(payload.symbol, payload.current_price)
        sentiment_score = get_sentiment_score(payload.symbol)
        recommendation = get_recommendation(predicted, payload.current_price)

        return {
            "predicted_price": predicted,
            "sentiment_score": sentiment_score,
            "recommendation": recommendation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ /sentiment
@app.post("/sentiment")
def sentiment_route(payload: SentimentRequest):
    try:
        score = get_sentiment_score(payload.symbol)
        return { "sentiment_score": score }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ /recommend
@app.post("/recommend")
def recommend_route(payload: RecommendationRequest):
    try:
        advice = get_recommendation(payload.predicted_price, payload.current_price)
        return { "recommendation": advice }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
