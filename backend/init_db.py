from models import db, Tracker
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/surveillance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Initialize the database
    db.create_all()

    # Insert sample data
    sample_trackers = [
        Tracker(name="Tracker 1", latitude=37.7749, longitude=-122.4194),
        Tracker(name="Tracker 2", latitude=34.0522, longitude=-118.2437),
        Tracker(name="Tracker 3", latitude=40.7128, longitude=-74.0060),
    ]

    db.session.add_all(sample_trackers)
    db.session.commit()

    print("Database initialized with sample data!")
