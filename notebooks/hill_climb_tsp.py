import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import time
from load_tsp import load_tsp

def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def get_neighbor(tour):
    new_tour = tour.copy()
    i, j = np.random.choice(len(tour), 2, replace=False)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def hill_climb(coords, dist_matrix, max_steps=1000):
    current_tour = list(np.random.permutation(len(coords)))
    current_distance = total_distance(current_tour, dist_matrix)
    history = [(current_tour.copy(), current_distance)]

    for step in range(max_steps):
        neighbor = get_neighbor(current_tour)
        neighbor_distance = total_distance(neighbor, dist_matrix)

        if neighbor_distance < current_distance:
            current_tour = neighbor
            current_distance = neighbor_distance
            history.append((current_tour.copy(), current_distance))

    return current_tour, current_distance, step + 1, history

def plot_tour(coords, tour, title):
    path = coords[tour + [tour[0]]]  # to make it a cycle
    plt.figure(figsize=(8, 6))
    plt.plot(path[:, 0], path[:, 1], 'o-', markersize=3)
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def animate_tour(coords, history, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot([], [], 'o-', lw=1.5)
    ax.set_xlim(coords[:, 0].min() - 10, coords[:, 0].max() + 10)
    ax.set_ylim(coords[:, 1].min() - 10, coords[:, 1].max() + 10)

    def update(frame):
        tour, dist = history[frame]
        path = coords[tour + [tour[0]]]
        line.set_data(path[:, 0], path[:, 1])
        ax.set_title(f"Step {frame + 1}, Distance: {dist:.2f}")
        return line,

    anim = FuncAnimation(fig, update, frames=len(history), interval=200, blit=True)
    anim.save(filename, writer=PillowWriter(fps=5))
    plt.close()

# --- Main Execution ---
if __name__ == "__main__":
    coords, dist_matrix = load_tsp("problems_cleaned/rat783.tsp")

    total_times = []
    total_distances = []

    best_overall_tour = None
    best_overall_distance = float('inf')
    best_history = []

    for run in range(5):
        start_time = time.time()
        tour, dist, steps, history = hill_climb(coords, dist_matrix)
        elapsed = time.time() - start_time

        total_times.append(elapsed)
        total_distances.append(dist)

        print(f"Run {run+1}: Best Distance = {dist:.2f}, Steps = {steps}, Time = {elapsed:.2f}s")

        if dist < best_overall_distance:
            best_overall_distance = dist
            best_overall_tour = tour
            best_history = history

    print(f"\nAverage Distance: {np.mean(total_distances):.2f}")
    print(f"Average Time: {np.mean(total_times):.2f}s")

    # Final plot and GIF of best run
    plot_tour(coords, best_overall_tour, "Best Hill Climb Tour")
    animate_tour(coords, best_history, "hill_climb_run1.gif")
