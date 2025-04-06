import gym
import time
import imageio
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def heuristic(state, goal, size):
    row_s, col_s = divmod(state, size)
    row_g, col_g = divmod(goal, size)
    return abs(row_s - row_g) + abs(col_s - col_g)

def ida_star(env):
    start = env.reset()[0]
    goal = env.desc.size - 1
    size = env.desc.shape[0]

    def dfs(path, g, bound, visited):
        node = path[-1]
        f = g + heuristic(node, goal, size)
        if f > bound:
            return f
        if node == goal:
            return path
        min_bound = float("inf")
        for action in range(env.action_space.n):
            for prob, next_state, reward, done in env.P[node][action]:
                if prob > 0 and next_state not in visited:
                    visited.add(next_state)
                    path.append(next_state)
                    result = dfs(path, g + 1, bound, visited)
                    if isinstance(result, list):
                        return result
                    if result < min_bound:
                        min_bound = result
                    path.pop()
                    visited.remove(next_state)
        return min_bound

    bound = heuristic(start, goal, size)
    path = [start]
    visited = set([start])
    while True:
        result = dfs(path, 0, bound, visited)
        if isinstance(result, list):
            return result
        if result == float("inf"):
            return None
        bound = result

# Run and record
if __name__ == "__main__":
    env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array")
    frames = []
    times = []

    for run in range(1):
        obs, _ = env.reset()
        start_time = time.time()
        path = ida_star(env)
        end_time = time.time()

        print(f"\nPath found: {path}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        print(f"Path length: {len(path)}")

        obs, _ = env.reset()
        frames.append(env.render())

        for s in path[1:]:
            for a in range(env.action_space.n):
                for prob, next_state, reward, done in env.P[obs][a]:
                    if next_state == s:
                        obs, _, _, _, _ = env.step(a)
                        frames.append(env.render())
                        break
                else:
                    continue
                break

    imageio.mimsave("ida_star_run.gif", frames, duration=0.5)
    print("GIF saved as ida_star_run.gif")
