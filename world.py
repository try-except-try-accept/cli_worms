
class World:

    def __init__(self):
        self.grid = self.create_scenary()




    def create_scenary(self):
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

    def display_scenary(self, scenary):
        for y, row in enumerate(scenary):
            for x, col in enumerate(row):
                lower_level = scenary[y+1][x] if y+1 < len(scenary) else ""
                if test_worm.x == x and test_worm.y == y:
                    if col == "/":
                        test_worm.y -= 1
                    elif lower_level == "\\":
                        test_worm.y += 1
                    print("S", end="")
                else:
                    print(col, end="")
            print()

