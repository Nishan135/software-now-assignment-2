import turtle
from recursive_edge import draw_pattern

def draw_polygon(sides, side_length, depth):
    angle = 360 / sides

    for _ in range(sides):
        draw_pattern(side_length, depth)
        turtle.right(angle)