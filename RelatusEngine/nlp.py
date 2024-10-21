from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes sentiment and returns a polarity score between -1 (negative) to 1 (positive).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity