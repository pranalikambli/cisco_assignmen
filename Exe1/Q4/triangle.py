import turtle

def triangle():

    TRIANGLE_SIZE = 200
    BORDER_SIZE = 3
    BORDER_SIZE1 = 2
    STAMP_UNIT = 20

    turtle.shape("triangle")
    turtle.hideturtle()
    turtle.penup()
    turtle.right(30)  # realign triangle
    turtle.fillcolor("#fff")
    turtle.shapesize(TRIANGLE_SIZE / STAMP_UNIT, TRIANGLE_SIZE / STAMP_UNIT, BORDER_SIZE)
    turtle.stamp()

    TRIANGLE_SIZE1 = 50
    turtle.fillcolor("#fff")
    y_offset = TRIANGLE_SIZE * 1 / 4
    turtle.goto(80, -y_offset)
    turtle.shapesize(TRIANGLE_SIZE1 / STAMP_UNIT, TRIANGLE_SIZE1 / STAMP_UNIT, BORDER_SIZE1)
    turtle.stamp()

    turtle.goto(-80, -y_offset)
    turtle.shapesize(TRIANGLE_SIZE1 / STAMP_UNIT, TRIANGLE_SIZE1 / STAMP_UNIT, BORDER_SIZE1)
    turtle.stamp()

    turtle.goto(0, 90)
    turtle.shapesize(TRIANGLE_SIZE1 / STAMP_UNIT, TRIANGLE_SIZE1 / STAMP_UNIT, BORDER_SIZE1)
    turtle.stamp()
    turtle.exitonclick()

triangle()
