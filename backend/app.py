from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import analyze_review

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

# 🔴 THIS PART IS REQUIRED FOR LOCAL TESTING
if __name__ == "__main__":
    app.run(debug=True, port=5000)

