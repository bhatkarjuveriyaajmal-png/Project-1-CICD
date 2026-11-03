
import logging
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to my DevOps CI/CD Project!",
        "status": "success",
        "project": "Project-1-CICD",
        "version": "1.0.0"
    }), 200


@app.get("/health")
def health():
    logger.info("Health check requested")
    return jsonify({
        "status": "healthy",
        "service": "Project-1-CICD"
    }), 200


@app.get("/greet")
def greet():
    name = request.args.get("name", "").strip()

    if not name:
        return jsonify({
            "error": "Name is required"
        }), 400

    if len(name) > 50:
        return jsonify({
            "error": "Name must be 50 characters or fewer"
        }), 400

    logger.info("Greeting request processed")

    return jsonify({
        "message": f"Hello, {name}!"
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=False)
