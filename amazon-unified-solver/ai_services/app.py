from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Amazon Unified Solver - AI Services",
        "endpoint": "/summarize"
    })

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")

    words = text.split()
    summary = " ".join(words[:20]) + ("..." if len(words) > 20 else "")

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
