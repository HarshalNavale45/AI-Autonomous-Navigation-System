from src.environment import create_grid, add_obstacles
from src.planner import astar
from src.visualizer import show_grid
from src.simulator import run_simulation

def main():
    grid = create_grid()
    grid = add_obstacles(grid)

    start = (0, 0)
    goal = (9, 9)

    path = astar(grid, start, goal)

    print("PATH:", path)

    show_grid(grid, path, start, goal)   # Static view
    run_simulation(grid, path, start, goal)  # Animation

if __name__ == "__main__":
    main()