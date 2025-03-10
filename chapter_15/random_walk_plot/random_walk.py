from random import choice

class RandomWalk:
    def __init__(self, num_points=5000, bias_x=False, bias_y=False, large_steps=False):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

        # Define step choices and direction bias
        self.step_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8] if large_steps else [0, 1, 2, 3, 4]
        self.x_directions = [1, -1] if not bias_x else [1]  # No left movement if bias_x=True
        self.y_directions = [1, -1] if not bias_y else [1]  # No downward movement if bias_y=True

    def get_step(self, directions, choices):
        """Generate a single step for x or y by choosing a direction and distance."""
        direction = choice(directions)  # Choose -1 or 1 (or just 1 if biased)
        distance = choice(choices)  # Choose step size
        return direction * distance  # Calculate step

    def fill_walk(self):
        """Generate points for the random walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step(self.x_directions, self.step_choices)
            y_step = self.get_step(self.y_directions, self.step_choices)

            # Skip steps that don't move anywhere
            if x_step == 0 and y_step == 0:
                continue  

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Append new points to the lists
            self.x_values.append(x)
            self.y_values.append(y)