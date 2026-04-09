import matplotlib.pyplot as plt

def show_grid(grid, path, start, goal):
    size = len(grid)

    plt.figure(figsize=(6,6))

    # Draw obstacles
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                plt.scatter(j, i, c='red', s=300)

    # Draw path
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, color='green', linewidth=3, marker='o', label="Path")

    # Start & Goal
    plt.scatter(start[1], start[0], c='yellow', s=400, label="Start")
    plt.scatter(goal[1], goal[0], c='purple', s=400, label="Goal")

    # Grid settings (IMPORTANT)
    plt.xticks(range(size))
    plt.yticks(range(size))
    plt.grid(True, linewidth=1)

    plt.xlim(-1, size)
    plt.ylim(-1, size)

    plt.title("Autonomous Navigation System (A*)")
    plt.legend()
    plt.gca().invert_yaxis()

    plt.show(block=False)
    plt.pause(1)
    plt.close()