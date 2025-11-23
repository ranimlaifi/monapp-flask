from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "123456")

limiter = Limiter(get_remote_address, app=app, default_limits=["10 per minute"])

# Comptage simple en mémoire (juste pour démo)
stats = {"200": 0, "403": 0, "404": 0}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/secret')
@limiter.limit("3 per minute")
def secret():
    key = request.headers.get('X-API-KEY')
    if key == API_KEY:
        stats["200"] += 1
        return jsonify({"message": "Accès autorisé !"})
    else:
        stats["403"] += 1
        return jsonify({"message": "Accès refusé !"}), 403
@app.errorhandler(404)
def page_not_found(e):
    stats["404"] += 1       # <--- AJOUT
    return "Page non trouvée", 404
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", stats=stats)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

