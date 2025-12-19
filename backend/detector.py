from textblob import TextBlob
import re

def repetition_score(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_ratio = len(set(words)) / max(len(words), 1)
    return round(unique_ratio * 100, 2)

def sentiment_score(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return round((polarity + 1) * 50, 2)  # Normalize 0–100

def credibility_score(text):
    rep = repetition_score(text)
    sent = sentiment_score(text)

    # Penalize extreme sentiment
    imbalance_penalty = abs(sent - 50)

    score = (rep * 0.6 + sent * 0.4) - imbalance_penalty * 0.3
    return max(0, min(100, round(score, 2)))

def analyze_review(text):
    return {
        "repetition_score": repetition_score(text),
        "sentiment_score": sentiment_score(text),
        "credibility_score": credibility_score(text),
        "is_suspicious": credibility_score(text) < 40
    }
