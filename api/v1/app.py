#!/usr/bin/python3
from api.v1.views import app_views
from flask import Flask
import os
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_storage(exception):
    """
    Close the storage object after the request is complete.
    """
    storage.close()

if __name__ == '__manin__':
    # Get host and port from environment variables or use defaults
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    
    # Start Flask server with specified options
    app.run(host=host, port=port, threaded=True)
