from flask import Flask, request, jsonify
from flask_cors import CORS
from model import train_model, predict, predict_proba

app = Flask(__name__)
CORS(app)

train_model("../dataset/dataset.csv")

@app.route("/")
def home():
    return "✅ API running"

@app.route("/predict", methods=["POST"])
def get_prediction():
    data = request.json
    text = data.get("text")

    sentiment = predict(text)
    confidence = predict_proba(text)

    return jsonify({
    "sentiment": sentiment,   # keep same key for frontend
    "confidence": round(confidence * 100, 2)})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)