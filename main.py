from random import randint
from os import system

print("""__    __ _____  _____ ___  __   __ 
\\ /\ //((   )) ||_// || \/ |  ((  
 \V/\V/  \\_//  || \\ ||    | \_)) """)

# plan

# create landscape

# add worm

# movement

# bomb!

HEIGHT = 30
WIDTH = 200
ENTRY = randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))

def create_scenary():

    grid = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]

    y = ENTRY

    draw = True
    try:
        for x in range(WIDTH):

            if draw:
                if not randint(0, 1):
                    # go straight
                    grid[y][x] = "_"

                elif not randint(0, 1):
                    # drop down
                    y += 1

                    grid[y][x] = "\\"

                else:
                    # go up
                    grid[y][x] = "/"
                    y -= 1


    except:
        pass


    return grid


def display_scenary(scenary):

    for y, row in enumerate(scenary):
        for x, col in enumerate(row):

            if test_worm.x == x and test_worm.y == y:
                print("S", end="")

            print(col, end="")
        print()


class Worm:
    def __init__(self):
        self.x = 0
        self.y = ENTRY

test_worm = Worm()

scenary = create_scenary()

while True:
    display_scenary(scenary)

    input()
    system("clear")
    test_worm.x += 1
    


