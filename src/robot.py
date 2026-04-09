# src/robot.py
from .planner import a_star

class Robot:
    def __init__(self, env):
        self.env = env
        self.current_pos = env.start
        self.goal_pos = env.goal
        self.steps = 0
        self.path = self.calculate_path()

    def calculate_path(self, start=None):
        if start is None:
            start = self.current_pos
        path = a_star(self.env.grid, start, self.goal_pos)
        return path