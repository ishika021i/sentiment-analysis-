from transformers import pipeline

# 🔥 Load models
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)


def train_model(file_path=None):
    print("✅ AI models loaded!")


# =========================
# EMOTION + SENTIMENT
# =========================
def predict(text):
    text_lower = text.lower()

    # 🔥 Empathy detection
    if "feel bad for" in text_lower or "feel sad for" in text_lower:
        return "empathy"

    # 🔥 Emotion detection
    emotion_result = emotion_pipeline(text)[0][0]
    emotion = emotion_result['label']
    score = emotion_result['score']

    # Map emotions to readable labels
    emotion_map = {
        "joy": "happy",
        "sadness": "sad",
        "anger": "angry",
        "fear": "fear",
        "surprise": "surprised",
        "neutral": "neutral"
    }

    detected_emotion = emotion_map.get(emotion, "neutral")

    return detected_emotion


# =========================
# CONFIDENCE
# =========================
def predict_proba(text):
    emotion_result = emotion_pipeline(text)[0][0]
    return emotion_result['score']