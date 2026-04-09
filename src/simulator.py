import pygame
import time

CELL_SIZE = 60
GRID_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

def run_simulation(grid, path, start, goal):
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
    pygame.display.set_caption("Autonomous Navigation Simulation")

    robot_pos = start

    running = True
    step = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if grid[i][j] == 1:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, BLACK, rect, 1)

        # Draw path
        for node in path:
            pygame.draw.circle(screen, GREEN,
                               (node[1]*CELL_SIZE + CELL_SIZE//2,
                                node[0]*CELL_SIZE + CELL_SIZE//2), 5)

        # Draw start & goal
        pygame.draw.circle(screen, YELLOW,
                           (start[1]*CELL_SIZE + CELL_SIZE//2,
                            start[0]*CELL_SIZE + CELL_SIZE//2), 10)

        pygame.draw.circle(screen, PURPLE,
                           (goal[1]*CELL_SIZE + CELL_SIZE//2,
                            goal[0]*CELL_SIZE + CELL_SIZE//2), 10)

        # Move robot
        if step < len(path):
            robot_pos = path[step]
            step += 1
            time.sleep(0.3)

        # Draw robot
        pygame.draw.circle(screen, BLUE,
                           (robot_pos[1]*CELL_SIZE + CELL_SIZE//2,
                            robot_pos[0]*CELL_SIZE + CELL_SIZE//2), 12)

        pygame.display.flip()

    pygame.quit()