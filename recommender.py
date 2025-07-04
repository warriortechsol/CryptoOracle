def get_recommendation(current_price, predicted_price, sentiment_score):
    delta = predicted_price - current_price
    threshold = 0.03 * current_price

    if delta > threshold and sentiment_score > 0.1:
        return "Buy"
    elif delta < -threshold and sentiment_score < -0.1:
        return "Sell"
    else:
        return "Hold"
