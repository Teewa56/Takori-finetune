from flask import Flask, request, jsonify
from finetune import build_prompt
import requests
import os
from flask_cors import CORS

API_URL = "https://tokari-core.onrender.com/api/v1/ai/chat-completion"
API_KEY = "tokari-0f8652c5-2fba-416e-9872-7e8387bf0af3";

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_question = request.json.get('question', '')
        if not user_question:
            return jsonify({"error": "No question provided."}), 400

        prompt = build_prompt(user_question)
        headers = {"x-api-key": API_KEY}
        payload = {"prompt": prompt}
        response = requests.post(API_URL, json=payload, headers=headers, timeout=20)
        response.raise_for_status()
        ai_answer = response.json().get('response', '')
        print(ai_answer)
        return jsonify({"answer": ai_answer})
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return jsonify({"error": "Failed to contact AI service."}), 502
    except Exception as e:
        print("Server error:", e)
        return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True)