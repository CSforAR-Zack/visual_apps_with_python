import turtle


def main():
    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]
    line_color: str = "white"

    t: turtle.Turtle = turtle.Turtle()
    s: turtle._Screen = turtle.Screen()

    t.speed(0)
    t.pensize(3)
    s.bgcolor("black")
    
    count: int = 16
    
    a: int = 0
    b: int = 1
    for num in range(count):
        c: int = a + b
        a = b
        b = c

        t.color(line_color, colors[num % len(colors)])

        t.begin_fill()
        for side in range(6):
            t.forward(c)
            t.left(90)
            if side == 3: # Square is complete
                t.end_fill()
        t.right(90)
        
        # t.end_fill() # Remove since moving up

    s.mainloop()


main()