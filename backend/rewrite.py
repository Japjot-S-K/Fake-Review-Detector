import re
from textblob import TextBlob

SPAM_PHRASES = [
    "buy now", "best ever", "amazing", "awesome",
    "highly recommend", "must buy", "five stars"
]

def clean_text(text):
    text = text.lower()
    for phrase in SPAM_PHRASES:
        text = re.sub(rf"\b{phrase}\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.6:
        return "The product works as expected and provides good value for its price."
    if polarity < -0.6:
        return "The product has some drawbacks, but overall it performs adequately."
    return text.capitalize()

def expand_short_review(text):
    if len(text.split()) < 8:
        return text + " The quality appears reasonable and delivery was on time."
    return text

def rewrite_review(text):
    cleaned = clean_text(text)
    normalized = normalize_sentiment(cleaned)
    expanded = expand_short_review(normalized)
    return expanded
