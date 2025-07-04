import pandas as pd
import joblib

def predict_price(symbol):
    model = joblib.load(f"models/{symbol}_model.pkl")
    df = pd.read_csv(f"backend/data/{symbol}_historical.csv")
    features = df[["Open", "High", "Low", "Volume"]].tail(30)
    prediction = model.predict(features)
    return float(prediction[-1])
