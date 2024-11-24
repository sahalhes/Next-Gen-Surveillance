from flask import Flask, jsonify, request
from gps_tracker import tracker

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Next Gen Surveillance!"

@app.route('/track', methods=['POST'])
def track_culprit():
    data = request.json
    result = tracker.track(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
