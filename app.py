from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "123456"  # Clé d'exemple pour l'authentification

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
