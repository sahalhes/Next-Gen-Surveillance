import sys
import os
from flask import Flask
from db import db  # Import db from db.py
from routes import api_routes

# Add parent directory to Python path so it can find the backend package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Example with SQLite, change for your DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

# Initialize db with the Flask app
db.init_app(app)

# Register API routes
app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
