from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
from src import training
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)

def delete_old_files(directory, age_minutes=30):
    now = time.time()
    age_seconds = age_minutes * 60

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > age_seconds:
                print(f"Deleting {file_path}")
                os.remove(file_path)

def scheduled_task():
    # Replace 'your_directory_path' with the path of the directory to clean up
    delete_old_files('videos', age_minutes=1)

# Set up the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'interval', minutes=1)
scheduler.start()

# Define directory for generated videos
VIDEO_DIR = 'videos'
os.makedirs(VIDEO_DIR, exist_ok=True)

@app.route('/')
def index():
    return jsonify({"message": "Ok"})

@app.route('/videos/<path:filename>', methods=['GET'])
def serve_video(filename):
    return send_from_directory(VIDEO_DIR, filename)

@app.route('/train', methods=['POST'])
def train():
    req = request.get_json()

    video_file = training.training_entrypoint(req)
    
    # return jsonify({"message": "Training started"})
    # return send_from_directory("videos", video_file)
    print(f"/{VIDEO_DIR}/{video_file}")
    return jsonify({"videoUrl": f"/{VIDEO_DIR}/{video_file}"})

@app.route('/testing', methods=['POST'])
def testing():
    time.sleep(10)
    return jsonify({"message": "Testing started"})

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()