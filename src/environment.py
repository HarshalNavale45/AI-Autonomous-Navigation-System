import numpy as np

def create_grid(size=10):
    return np.zeros((size, size))

def add_obstacles(grid):
    obstacles = [(3,3), (3,4), (3,5), (6,7), (7,7)]
    for x, y in obstacles:
        grid[x][y] = 1
    return grid