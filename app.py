from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

@app.route('/')
def home():
    return "Bienvenue sur mon application Flask PaaS !"

@app.route('/secret')
def secret():
    key = request.headers.get('X-API-KEY')
    if key == API_KEY:
        return jsonify({"message": "Accès autorisé !"})
    else:
        return jsonify({"message": "Accès refusé !"}), 401

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

