from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

# APIキーを環境変数から取得
openai.api_key = os.getenv("OPEN_API_KEY")

app = Flask(__name__)

# MonacaからのCORSを許可
#CORS(app, supports_credentials=True)
CORS(app, origins=["https://console.monaca.education"])

@app.route("/api/chat", methods=["POST", "OPTIONS"])
def chat():
    # プリフライトリクエスト対応（CORS対策）
    if request.method == "OPTIONS":
        return '', 204

    # POSTリクエスト処理
    data = request.get_json()
    message = data.get("message", "")
    reply = f"あなたは「{message}」と言いましたね"
    return jsonify({"reply": reply})

#def chat():
#    user_message = request.json.get("message")
#    try:
#        response = openai.ChatCompletion.create(
#            model = "gpt-4",
#            messages = [{"role": "user", 
#                        "content": user_message}]
#        )
#        return jsonify(response)
#    except Exception as e:
#        return jsonify({"error": str(e)}), 500

#if __name__ == "__main__":
#        app.run()