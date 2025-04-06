# AI_Assignment_2
# Search and Optimization Algorithms for FrozenLake & TSP

This project implements and compares the performance of four algorithms on two different environments:
- **FrozenLake** (Discrete Grid World) using OpenAI Gym
- **Traveling Salesman Problem (TSP)** using `.tsp` coordinate files

## Algorithms Implemented

### 1. Branch and Bound (FrozenLake)
A best-first search approach using a priority queue to explore the least-cost paths first.
-  Deterministic, non-slippery FrozenLake
-  Cost = path length
-  Goal: reach the terminal state minimizing cost

### 2. Iterative Deepening A* (IDA*) (FrozenLake)
Combines the space efficiency of DFS with the optimality of A*.
-  Uses Manhattan distance as a heuristic
-  Reduces memory footprint compared to A*
-  Repeats DFS with increasing cost bounds

### 3. Hill Climbing (TSP)
A local search heuristic that iteratively improves a solution by exploring neighbors.
-  Starts from a random tour
-  Accepts better neighbors only
-  Fast but may get stuck in local optima
-  Animated results and time logging included

### 4. Simulated Annealing (TSP)
A probabilistic technique to escape local optima.
-  Starts hot and slowly cools down
-  Sometimes accepts worse solutions early on
-  Balances exploration and exploitation
-  GIF recording and convergence logs included

---

##  Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

Create and activate the virtual environment: python -m venv tsp-env .\tsp-env\Scripts\activate
Install dependencies: pip install -r requirements.txt

## Usage
Run Branch and Bound : python branch_and_bound.py
Run IDA*             : python ida_star.py
Run Hill Climbing for TSP : python hill_climb_tsp.py
Run Simulated Annealing for TSP : python simulated_annealing_tsp.py

 

 
