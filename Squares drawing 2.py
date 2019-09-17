from turtle import *

fillcolor('purple')
pensize(10)
pencolor('black')
speed(0)

for cubeplusplusplus in range(2):
    for cubeplusplus in range(2):
        for cubeplus in range(2):
            for cube in range(3):
                for square in range(3):
                    begin_fill()
                    forward(100)
                    left(90)
                    forward(100)
                    left(90)
                    forward(100)
                    left(90)
                    forward(100)
                    left(90)
                    end_fill()
                    forward(100)

                left(180)
                forward(300)
                right(90)
                forward(100)
                right(90)

            home()
            right(90)

        right(90)

    right(90)
