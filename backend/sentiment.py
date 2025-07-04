import requests
from textblob import TextBlob

def get_sentiment_score(symbol):
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey=YOUR_NEWSAPI_KEY"
    response = requests.get(url).json()
    articles = response.get("articles", [])
    scores = [TextBlob(article["title"]).sentiment.polarity for article in articles]
    return sum(scores) / len(scores) if scores else 0
