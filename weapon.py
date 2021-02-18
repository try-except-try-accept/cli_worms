from config import *
from sprite import Sprite

class Weapon(Sprite):

    def __init__(self, x, y, grid, destructor ):

        super().__init__(x, y, '', False)
        super().set_grid(grid)
        self.explosion_queue = list(EXPLOSIONS)
        self.destructor = destructor
        self.existence = 0


    def delete(self):
        self.destructor(self)





class Arrow(Weapon):

    def __init__(self, x, y, grid, destructor):
        super().__init__(x, y, grid, destructor)



    def fire(self, cmd, direction):

        c_points = len(ORIENTATIONS)

        self.existence += 1

        octile = int(8 * (direction / c_points))

        angle = int(len(ANGLES) * (direction / c_points))

        x_vel = ANGLES[angle][0]
        y_vel = ANGLES[angle][1]

#         print("""direction {}
# octile {}
# x_vel {}
# y_vel {}""".format(direction, octile, x_vel, y_vel))

        self.symbol = D_MAP[octile][2]

        self.x += x_vel
        self.y += y_vel
        max_velocity = max([1, abs(x_vel), abs(y_vel)])

        #input(str("max vel is {}".format(max_velocity)))

        frame_rate = FRAME_SPEED*max_velocity


        if self.check_out_of_bounds(check_top=True, check_bottom=True, check_horiz=True, out_of_bounds_next_step=self.delete):
            return 0, STOP_ANIMATION

        if self.existence > ARROW_LIFE:
            self.visible = False
            return frame_rate, -1

        if self.grid[self.y][self.x] != " ":
            if len(self.explosion_queue):
                self.symbol = self.explosion_queue.pop(0)
            else:
                self.visible = False
                return frame_rate, -1



        return frame_rate, direction

