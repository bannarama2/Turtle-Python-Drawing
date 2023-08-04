import turtle

pen = turtle.Turtle()

pen.speed(10000000)

def circle():
    
    pen.fillcolor("pink")
    pen.begin_fill()

    for i in range(360):
        pen.forward(1)
        pen.right(1)
        
    pen.up()

    pen.forward(115)

    pen.down()

    for j in range(360):
        pen.forward(1)
        pen.right(1)

    pen.up()

    pen.back(115)

    pen.down()
    
    pen.right(500)

    for x in range(360):
        pen.forward(1)
        pen.right(1)

    pen.end_fill()

    

circle()

turtle.Screen().exitonclick()