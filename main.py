from The_class import SeasonTree
import turtle

tree = SeasonTree()

# Position the turtle at the desired starting location
tree.t.penup()
tree.t.goto(0, -250)  # Positioning the turtle at the bottom center of the screen
tree.t.left(90)  # Pointing the turtle upwards to start drawing the tree
tree.t.pendown()

tree.draw_tree(100)
turtle.done()
