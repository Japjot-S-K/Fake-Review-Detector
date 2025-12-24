from textblob import TextBlob
import re

def repetition_score(text):
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return 0
    unique_ratio = len(set(words)) / len(words)
    return round(unique_ratio * 100, 2)

def sentiment_score(text):
    polarity = TextBlob(text).sentiment.polarity
    return round((polarity + 1) * 50, 2)  # 0–100

def explain_review(text):
    reasons = []

    rep = repetition_score(text)
    sent = sentiment_score(text)
    word_count = len(text.split())

    if rep < 50:
        reasons.append("Repeated or low-diversity language detected")

    if sent > 80:
        reasons.append("Overly positive sentiment detected")

    if sent < 20:
        reasons.append("Overly negative sentiment detected")

    if word_count < 8:
        reasons.append("Review is too short and lacks detail")

    if not reasons:
        reasons.append("Language and sentiment appear natural")

    return reasons

def credibility_score(text):
    rep = repetition_score(text)
    sent = sentiment_score(text)
    imbalance_penalty = abs(sent - 50)
    score = (rep * 0.6 + sent * 0.4) - imbalance_penalty * 0.3
    return max(0, min(100, round(score, 2)))

def analyze_review(text):
    score = credibility_score(text)
    return {
        "repetition_score": repetition_score(text),
        "sentiment_score": sentiment_score(text),
        "credibility_score": score,
        "is_suspicious": score < 40,
        "reasons": explain_review(text)
    }
