from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure the generative AI model
genai.configure(api_key="AIzaSyB5mJWNfjiCMXpIdVPfS1mVmrvM31bRKYA")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Function to generate a response
def GenerateResponse(input_text):
    response = model.generate_content([
        "You are a style and fashion advisor chatbot so reply accordingly...",
        f"input: {input_text}",
        "output: "
    ])
    return response.text.strip()

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    bot_reply = GenerateResponse(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
