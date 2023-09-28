import turtle
import random


current_season = "spring"  # global variable

def draw_tree(branch_len, t):
    angle = random.randint(15, 25) 
    length_factor = random.uniform(0.6, 0.8) # "uniform" --> random decimal

    if branch_len > 5:

        if current_season == "spring":
            t.color("brown", "lightgreen")
        elif current_season == "summer":
            t.color("brown", "green")
        elif current_season == "autumn":
            t.color("brown",random.choice(["orange", "yellow", "red"]))
        else: # winter
            t.color("lightgray", "white")            

        t.forward(branch_len)

        t.right(angle)
        draw_tree(branch_len * length_factor, t)  # the right branch

        t.left(2 * angle)
        draw_tree(branch_len * length_factor, t)  # the left branch 

        t.right(angle)
        t.backward(branch_len)

    else:
        t.dot()


