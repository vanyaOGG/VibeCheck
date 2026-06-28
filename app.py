import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
from emotion import predict_emotion
from music import fetch_tracks

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    try:
        text = data['text']
        label, confidence = predict_emotion(text)
        tracks = fetch_tracks(label)
        return jsonify({
            "emotion": label,
            "confidence": round(confidence, 4),
            "tracks": tracks
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)