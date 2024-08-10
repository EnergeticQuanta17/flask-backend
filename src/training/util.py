import os
import gymnasium as gym

# TODO: It is not returning the correct version check again
def find_latest_version(env_name):
    env_specs = gym.envs.registry
    # print(env_specs)
    cartpole_versions = [spec.id for spec in env_specs.values() if env_name in spec.id]
    print(cartpole_versions)

    # Get the latest version
    latest_version = sorted(cartpole_versions, key=lambda x: int(x.split('-v')[-1]))[-1]

    return latest_version

# TODO: video for another user might be returned to another user
def find_latest_video(folder_dir):
    videos = [f for f in os.listdir(folder_dir) if f.endswith(".mp4")]
    latest_video = sorted(videos, key=lambda x: int(x.split('-')[-1].split('.')[0]))[-1]

    return latest_video