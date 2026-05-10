from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Amazon Unified Solver - Security Module",
        "endpoint": "/check"
    })

@app.route('/check', methods=['POST'])
def check_message():
    data = request.get_json()
    message = data.get("message", "").lower()

    scam_keywords = ["lottery", "prize", "winner", "free money", "urgent", "click here"]

    if any(word in message for word in scam_keywords):
        return jsonify({"result": "Likely Scam ❌"})
    else:
        return jsonify({"result": "Safe ✅"})

if __name__ == "__main__":
    app.run(debug=True)
