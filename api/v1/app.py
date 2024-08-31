#!/usr/bin/python3
"""Imported modules"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
import os

app = Flask(__name__)


"""Register Blueprint"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """method that calls storage"""
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """Returns JSON 404 response"""
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
