from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

# Define directory for generated videos
VIDEO_DIR = 'static/videos'
os.makedirs(VIDEO_DIR, exist_ok=True)

@app.route('/run', methods=['GET'])
def run_rl():
    return jsonify({"message": "OK"})

@app.route('/run', methods=['GET'])
def run_rl():
    # data = request.get_json()
    
    video_url = f"/static/videos/countdown.mp4"
    return jsonify({'videoUrl': video_url})

@app.route('/static/videos/<path:filename>', methods=['GET'])
def serve_video(filename):
    return send_from_directory(VIDEO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)