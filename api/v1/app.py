#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views

# Create a new Flask app instance
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(error=None):
  """
    Close the storage connection on app context teardown.

    Args:
        error (Exception): The exception that caused the teardown, if any.

    Returns:
        None
    """
  storage.cose()

if __name__ == '__main__':
  # Get host and port from environment variables or use defaults
  host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
  port = int(os.environ.get('HBNB_API_PORT', 5000))

  # Start Flask server with specified options
  app.run(host=host, port=port, threaded=True)

@app.errorhandler(404) #error handler
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)
