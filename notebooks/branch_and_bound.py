import gym
import heapq
import time
import warnings
import imageio

warnings.filterwarnings("ignore", category=DeprecationWarning)

def branch_and_bound(env):
    start_state = env.reset()[0]
    goal_state = env.desc.size - 1  # Last cell in the grid
    visited = set()

    # Priority queue: (cost_so_far, state, path)
    queue = [(0, start_state, [])]

    while queue:
        cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal_state:
            return path  # Found goal

        for action in range(env.action_space.n):
            for prob, next_state, reward, done in env.P[state][action]:
                if prob > 0 and next_state not in visited:
                    heapq.heappush(queue, (cost + 1, next_state, path))

    return None  # No solution found

if __name__ == "__main__":
    env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="rgb_array")

    start = time.time()
    path = branch_and_bound(env)
    end = time.time()

    print("\nPath found:", path)
    print(f"Time taken: {end - start:.4f} seconds")
    print(f"Path length: {len(path)}")

    # Record the path as a GIF
    obs, _ = env.reset()
    frames = [env.render()]
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

    gif_path = "branch_and_bound_run.gif"
    imageio.mimsave(gif_path, frames, duration=0.5)
    print(f"GIF saved as {gif_path}")
