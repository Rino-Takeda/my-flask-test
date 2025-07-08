from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

#APIキーを環境変数から取得(Azureに設定)
openai.api_key = os.getenv("OPEN_API_KEY")

app = Flask(__name__)
CORS(app) #manacaからのアクセスを許可

@app.route("/api/chat", 
methods=["POST"])
def chat():
    user_message = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [{"role": "user", 
                        "content": user_message}]
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
        app.run()