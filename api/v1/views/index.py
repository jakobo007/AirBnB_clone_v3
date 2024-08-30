#!/usr/bin/python3
"""imported modules"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """returns a JSON"""
    return jsonify({"status": "OK"})
