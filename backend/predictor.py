import requests
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def predict_price(symbol: str, current_price: float):
    try:
        print(f"[DEBUG] predict_price called with symbol={symbol}, current_price={current_price}")

        # 🔗 CoinGecko symbol mapping
        symbol_to_id = {
            "BTC": "bitcoin",
            "ETH": "ethereum",
            "SOL": "solana",
            "DOGE": "dogecoin",
            "ADA": "cardano"
        }

        if symbol not in symbol_to_id:
            raise ValueError(f"Unsupported symbol: {symbol}")

        # 🌐 Fetch historical data
        url = f"https://api.coingecko.com/api/v3/coins/{symbol_to_id[symbol]}/market_chart"
        params = {"vs_currency": "usd", "days": "90"}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise ValueError(f"CoinGecko API failed: {response.status_code} - {response.text}")

        data = response.json()
        prices = [p[1] for p in data["prices"]]
        volumes = [v[1] for v in data["total_volumes"]]

        df = pd.DataFrame({
            "Close": prices,
            "Volume": volumes
        })

        df["Return"] = df["Close"].pct_change().fillna(0)
        df["Volatility"] = df["Return"].rolling(window=7).std().fillna(0)

        features = df[["Close", "Volume", "Volatility"]].tail(30)
        targets = df["Close"].shift(-1).dropna().tail(30)

        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(features)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_scaled, targets)

        X_next = scaler.transform([features.iloc[-1].values])
        prediction = model.predict(X_next)[0]

        print(f"[DEBUG] Prediction result: {prediction}")
        return round(prediction, 2)

    except Exception as e:
        print(f"[ERROR] predict_price crashed: {e}")
        raise

