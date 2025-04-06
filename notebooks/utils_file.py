# utils.py
import time
import imageio
import matplotlib.pyplot as plt

def record_gif(frames, filename="run.gif"):
    """Save frames as an animated GIF."""
    imageio.mimsave(filename, frames, fps=2)

def log_performance(start_time, path):
    """Print time taken and path length."""
    duration = time.time() - start_time
    print(f"\nTime taken: {duration:.4f} seconds")
    print(f"Path length: {len(path)}")

def manhattan_distance(pos1, pos2, width):
    """Heuristic: Manhattan distance for grid-based envs."""
    x1, y1 = pos1 % width, pos1 // width
    x2, y2 = pos2 % width, pos2 // width
    return abs(x1 - x2) + abs(y1 - y2)
