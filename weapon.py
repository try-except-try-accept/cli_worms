from config import *

class Weapon:

    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
        self.visible = True
        self.explosion_queue = '''☆
✰
٭
✯
✭
✵
✪
⚝'''.split("\n")





class Arrow(Weapon):

    def __init__(self, x, y, grid):
        super().__init__(x, y, grid)




    def fire(self, cmd, direction):
        self.x += D_MAP[direction][0]
        self.y += D_MAP[direction][1]
        self.symbol = D_MAP[direction][2]


        if self.grid[self.y][self.x] != " ":
            if len(self.explosion_queue):
                self.symbol = self.explosion_queue.pop(0)
            else:
                self.visible = False
                return 0.125, 0

        return 0.125, direction

