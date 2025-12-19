from flask import Flask, request, jsonify
from detector import analyze_review
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Fake Review Detector API running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    review = data.get("review", "")
    return jsonify(analyze_review(review))
