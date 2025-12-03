from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load model emotion detection sekali di awal
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text_to_analyze", "").strip()
        if input_text:
            # Model mengembalikan list skor emosi
            scores = emotion_classifier(input_text)[0]  # list of dict: [{'label': 'joy', 'score': ...}, ...]
            emotions = {s["label"]: float(s["score"]) for s in scores}
            dominant_emotion = max(emotions, key=emotions.get)

            result = {
                "emotions": emotions,
                "dominant": dominant_emotion
            }

    return render_template("index.html", result=result, input_text=input_text)


if __name__ == "__main__":
    # Kalau di lab IBM biasanya pakai host='0.0.0.0'
    app.run(host="0.0.0.0", port=5000, debug=True)
