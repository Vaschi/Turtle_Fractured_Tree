import turtle
import random

class SeasonTree:

    def __init__(self):
        # 1. Building the turtle
        self.t = turtle.Turtle()
        self.t.speed(0)
        
        # 2. Setting up the screen
        self.screen = turtle.Screen()
        self.screen.title("Fractal Tree")
        self.screen.setup(width=800, height=600)  # Define screen width and height
        self.screen.bgcolor("white")

    def draw_tree(self, branch_len):
        angle = random.randint(15, 25)
        length_factor = random.uniform(0.6, 0.8)

        if branch_len > 5:
            self.t.forward(branch_len)
            self.t.right(angle)
            self.draw_tree(branch_len * length_factor)
            self.t.left(2 * angle)
            self.draw_tree(branch_len * length_factor)
            self.t.right(angle)
            self.t.backward(branch_len)
        else:
            self.t.dot()

# No display function, you can call the methods separately in the main script.
