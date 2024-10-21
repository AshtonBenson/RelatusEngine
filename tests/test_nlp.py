import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import RelatusEngine.nlp as nlp

def test_analyze_sentiment_positive():
    dialogue = "You are an amazing person!"
    sentiment = nlp.analyze_sentiment(dialogue)
    assert sentiment > 0, f"Expected positive sentiment, got {sentiment}"

def test_analyze_sentiment_negative():
    dialogue = "I hate this situation. You're terrible!"
    sentiment = nlp.analyze_sentiment(dialogue)
    assert sentiment < 0, f"Expected negative sentiment, got {sentiment}"

def test_analyze_sentiment_neutral():
    dialogue = "It's nothing special."
    sentiment = nlp.analyze_sentiment(dialogue)
    
    neutral_range = (-0.36, 0.36)
    
    assert neutral_range[0] <= sentiment <= neutral_range[1], f"Expected neutral sentiment, got {sentiment}"

def test_analyze_sentiment_mixed():
    dialogue = "I love how you try, but sometimes you mess things up."
    sentiment = nlp.analyze_sentiment(dialogue)
    assert -0.2 < sentiment < 0.2, f"Expected mixed/neutral sentiment, got {sentiment}"

def test_analyze_sentiment_complex():
    dialogue = "I appreciate your effort, but this is not good at all."
    sentiment = nlp.analyze_sentiment(dialogue)
    assert sentiment < 0, f"Expected negative sentiment for complex feedback, got {sentiment}"
