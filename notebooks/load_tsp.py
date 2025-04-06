import numpy as np

def load_tsp(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    coords_start = False
    coords = []
    for line in lines:
        if 'NODE_COORD_SECTION' in line:
            coords_start = True
            continue
        if 'EOF' in line or line.strip() == '':
            break
        if coords_start:
            parts = line.strip().split()
            if len(parts) >= 3:
                coords.append([float(parts[1]), float(parts[2])])

    coordinates = np.array(coords)
    n = len(coordinates)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = np.linalg.norm(coordinates[i] - coordinates[j])

    return coordinates, distance_matrix
