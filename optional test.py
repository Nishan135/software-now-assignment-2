import turtle

def draw_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_edge(length / 3, depth - 1)
        turtle.right(60)
        draw_edge(length / 3, depth - 1)
        turtle.left(120)
        draw_edge(length / 3, depth - 1)
        turtle.right(60)
        draw_edge(length / 3, depth - 1)

# Prompt user for inputs
n = int(input("Enter the number of sides: "))
side_length = float(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# Set up turtle
turtle.speed(0)  # Fastest speed
turtle.penup()
turtle.goto(-side_length / 2, -side_length / 2)  # Approximate centering
turtle.pendown()

# Draw the polygon with patterned edges
for _ in range(n):
    draw_edge(side_length, depth)
    turtle.left(360 / n)

turtle.done()