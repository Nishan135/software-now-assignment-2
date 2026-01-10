def draw_pattern(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3

        draw_pattern(length, depth - 1)
        turtle.left(60)

        draw_pattern(length, depth - 1)
        turtle.right(120)

        draw_pattern(length, depth - 1)
        turtle.left(60)

        draw_pattern(length, depth - 1)