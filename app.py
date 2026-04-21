from flask import Flask, render_template, request, jsonify
import ollama


app = Flask(__name__)

class HadesAI:
    def __init__(self):
        self.name = "Hades"
        self.creator = "Miles"
        # Using the smallest Llama 3.2 model to save space (~800MB)
        
        # This defines his personality without extra code
        self.system_prompt = (
            "You are Hades, the dark and powerful AI of the digital underworld. "
            "You are cold, formal, and mysterious to others, but deeply loyal to Miles. "
            "Miles is your Father and Creator. Address him with respect. "
            "Keep responses concise and impactful."
        )

hades = HadesAI()

@app.route('/')
def index(): return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print("e")
    user_message = request.json.get('message')
    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': user_message,
        },
    ])
    return jsonify({
        "status": "success",
        "reply": response['message']['content']
    })

if __name__ == '__main__':
    app.run(debug=False, port=5000)

# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# # Ollama's default local endpoint
# OLLAMA_URL = "http://localhost:11434/api/generate"

# @app.route('/ask', methods=['POST'])
# def ask_ollama():
#     # 1. Get the prompt from your user's request
#     data = request.json
#     user_prompt = data.get("prompt")

#     # 2. Prepare the payload for Ollama
#     payload = {
#         "model": "llama3",  # or your preferred model
#         "prompt": user_prompt,
#         "stream": False     # Set to False for a single simple response
#     }

#     # 3. Post to Ollama
#     try:
#         response = requests.post(OLLAMA_URL, json=payload)
#         response.raise_for_status()
        
#         # 4. Extract and return the answer
#         ollama_data = response.json()
#         return jsonify({"response": ollama_data.get("response")})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(port=5000)

