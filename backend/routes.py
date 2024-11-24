from flask import Blueprint, jsonify
from models import db, Tracker

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/track', methods=['GET'])
def get_trackers():
    trackers = Tracker.query.all()
    result = [{"id": t.id, "name": t.name, "latitude": t.latitude, "longitude": t.longitude, "timestamp": t.timestamp.isoformat()} for t in trackers]
    return jsonify(result)

@api_routes.route('/track', methods=['POST'])
def add_tracker():
    # Example: This would typically come from a request body
    tracker_data = {
        'name': 'Suspect 1',
        'latitude': 40.7128,
        'longitude': -74.0060,
        'timestamp': '2024-11-24T10:00:00',
    }

    new_tracker = Tracker(
        name=tracker_data['name'],
        latitude=tracker_data['latitude'],
        longitude=tracker_data['longitude'],
        timestamp=tracker_data['timestamp'],
    )

    db.session.add(new_tracker)
    db.session.commit()

    return jsonify({"message": "Tracker added successfully!"}), 201
