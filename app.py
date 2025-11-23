from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Rate limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/secret')
@limiter.limit("3 per minute")
def secret():
    key = request.headers.get('X-API-KEY')
    if key == API_KEY:
        return jsonify({"message": "Accès autorisé !"})
    else:
        return jsonify({"message": "Accès refusé !"}), 403

if __name__ == "__main__":
    app.run(debug=True)

