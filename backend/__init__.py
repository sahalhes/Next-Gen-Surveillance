from flask import Flask
from backend.models import db
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)
