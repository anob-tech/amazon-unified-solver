from flask import Flask, jsonify, request

app = Flask(__name__)

questions = [
    {"id": 1, "question": "What is phishing?", "options": ["Email scam", "Fish farming", "Data backup"], "answer": "Email scam"},
    {"id": 2, "question": "Strong password should include?", "options": ["Only letters", "Letters, numbers, symbols", "Your name"], "answer": "Letters, numbers, symbols"},
    {"id": 3, "question": "What should you do if you get a suspicious link?", "options": ["Click immediately", "Ignore/delete", "Forward to friends"], "answer": "Ignore/delete"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Amazon Unified Solver - Training Game",
        "endpoints": {
            "/questions": "List all quiz questions",
            "/answer": "Submit answer"
        }
    })

@app.route('/questions')
def list_questions():
    return jsonify(questions)

@app.route('/answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    qid = data.get("id")
    user_answer = data.get("answer")

    question = next((q for q in questions if q["id"] == qid), None)
    if question:
        if user_answer == question["answer"]:
            return jsonify({"result": "Correct ✅"})
        else:
            return jsonify({"result": "Wrong ❌"})
    else:
        return jsonify({"error": "Question not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
