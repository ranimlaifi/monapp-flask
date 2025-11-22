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
    app.run(debug=True)

