from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.predictor import predict_price
from backend.sentiment import get_sentiment_score
from backend.recommender import get_recommendation

app = FastAPI()

# ✅ CORS setup for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 Consider restricting in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ✅ Root handler (optional but helpful)
@app.get("/")
def root():
    return {"message": "CryptoOracle backend is online."}

# ✅ Favicon fallback (optional)
@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon here — this is an API."}

# ✅ Pydantic models
class PredictionRequest(BaseModel):
    symbol: str
    current_price: float

class SentimentRequest(BaseModel):
    symbol: str

class RecommendationRequest(BaseModel):
    predicted_price: float
    current_price: float

# ✅ Predict endpoint
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

# ✅ Sentiment endpoint
@app.post("/sentiment")
def sentiment_route(payload: SentimentRequest):
    try:
        score = get_sentiment_score(payload.symbol)
        return { "sentiment_score": score }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ Recommendation endpoint
@app.post("/recommend")
def recommend_route(payload: RecommendationRequest):
    try:
        advice = get_recommendation(payload.predicted_price, payload.current_price)
        return { "recommendation": advice }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

