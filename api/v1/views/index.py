#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

@app_views.route(/status)
def status():
  """
  Return a JSON response indicating that the API status is OK.

  Returns:
    dict: A JSON response with the status key set to OK.
  """
  return jsonify({'status': 'OK'})
