from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import analyze_review
from rewrite import rewrite_review


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

@app.route("/rewrite", methods=["POST"])
def rewrite():
    data = request.json
    review = data.get("review", "")
    improved = rewrite_review(review)
    return jsonify({"rewritten_review": improved})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

