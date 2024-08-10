import gymnasium as gym # type: ignore
import subprocess
import cv2 # type: ignore
import uuid

from .util import *

def training_entrypoint(req):
    env_name = req['environment']
    number_of_frames = 100

    unique_id = str(uuid.uuid4())[:8]

    video_file_name = f"{env_name}_{number_of_frames}_{unique_id}.mp4"
    # video_file_name = "output.mp4"

    command = ["python", "video_recorder.py", env_name, f"videos/{video_file_name}", "1000"]
    subprocess.run(command)

    return video_file_name
