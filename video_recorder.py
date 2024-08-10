import cv2
import gymnasium as gym
import random
import time
import sys

def main(env_name, output_file, num_frames):
    env = gym.make(env_name, render_mode="rgb_array")
    env.reset()

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_file, fourcc, 30.0, (env.render().shape[1], env.render().shape[0]))

    try:
        start_time = time.perf_counter()

        observation, info = env.reset()
        print(env.render().shape)

        for i in range(num_frames):
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)
            frame = env.render()
            out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)) 
        print(action)   
    finally:
        print("out released", out.release())
        env.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <env_name> <output_file> <num_frames>")
    else:
        env_name = sys.argv[1]
        output_file = sys.argv[2]
        num_frames = int(sys.argv[3])
        main(env_name, output_file, num_frames)
