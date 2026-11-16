from flask import Blueprint, jsonify  # explanation - import Blueprint and jsonify from the flask package

main_bp = Blueprint('main', __name__)  # explanation - create a blueprint named "main"

@main_bp.route("/health", methods=["GET"])  # explanation - connect GET /health requests to the function below

def health():  # explanation - this function runs whenever a GET request comes to /health
    return jsonify({"status": "ok"}), 200  # explanation - send back JSON with status "ok" and HTTP 200 (success)