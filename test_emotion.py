from app import emotion_classifier

def test_emotion_detection():
    text = "I am very happy today"
    result = emotion_classifier(text)[0]
    
    emotions = {item["label"]: item["score"] for item in result}
    dominant = max(emotions, key=emotions.get)

    assert dominant in emotions
    print("Test passed. Dominant emotion:", dominant)

if __name__ == "__main__":
    test_emotion_detection()
