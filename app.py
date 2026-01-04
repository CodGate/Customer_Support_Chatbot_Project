
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def chatbot_response(user_input):
    text = user_input.lower()

    if "refund" in text:
        return "I understand your concern. Please share your order ID so I can assist you with the refund."
    elif "order" in text or "track" in text:
        return "Sure! Please provide your order ID to track your order."
    elif "login" in text or "account" in text:
        return "If you're facing login issues, please try resetting your password."
    elif "angry" in text or "bad" in text:
        return "I’m really sorry for the inconvenience. I’m here to help you."
    else:
        return "Thank you for contacting support. Could you please clarify your issue?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)

