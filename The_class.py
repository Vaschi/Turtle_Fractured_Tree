import turtle
import random

class SeasonTree:

    def __init__(self):
        # Building the turtle
        self.t = turtle.Turtle()
        self.t.speed(0)
        
        # Setting up the screen
        self.screen = turtle.Screen()
        self.screen.title("Fractal Tree")
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("white")
        
        # Positioning the turtle at the start
        self.t.penup()
        self.t.goto(0, -250)  # Positioning the turtle at the bottom center
        self.t.left(90)  # Pointing the turtle upwards
        self.t.pendown()

        self.current_season = "spring"  # Default season

    def set_season(self, season):
        """Set the current season."""
        self.current_season = season
   
    def get_season_color(self):
        """Return colors based on the season."""
        if self.current_season == "spring":
            return "brown", "lightgreen"
        elif self.current_season == "summer":
            return "brown", "green"
        elif self.current_season == "autumn":
            return "brown", random.choice(["orange", "yellow", "red"])
        elif self.current_season == "winter":
            return "lightgray", "white"
        else:
            return "brown", "lightgreen"  # default


    def draw_tree(self, branch_len):
        trunk_color, leaf_color = self.get_season_color()
        self.t.color(trunk_color)

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
            self.t.dot(10,leaf_color)

