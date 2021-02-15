
from config import *
from helpers import get_death_msg, get_gravestone, get_boundary_msg
from random import randint, choice as rand_choice

class Worm:
    def __init__(self, name, team, start_x, symbol, msg_queue):
        self.msgs = msg_queue
        self.name = name
        self.team = team
        self.symbol = symbol
        self.x = start_x
        self.y = randint(-WORMS_PER_TEAM, 0)
        self.dead = False
        self.visible = False
        self.jump_queue = []
        self.jumping = False
        self.frame_speed = FRAME_SPEED
        self.falling = False
        self.gender = rand_choice(["male", "female"])

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        '''Allow leftmost worm to be selected for testing'''
        return self.x < other.x

    def check_out_of_bounds(self, check_horiz=True):
        if not check_horiz:
            if self.y > HEIGHT-2:
                self.y = HEIGHT-2
                return True
            elif self.y < 0:
                self.y = 0
                return True
        else:
            if self.x > WIDTH - 1:
                self.msgs.append(get_boundary_msg(self.name, self.gender))
                self.x = WIDTH - 1
                return True
            elif self.x < 0:
                self.msgs.append(get_boundary_msg(self.name, self.gender))
                self.x = 0
                return True
        return False

    def fall(self):
        '''Increase y axis to fall, return True if make contact
        with scenery - False if not yet'''
        if self.dead:   return True

        if self.grid[self.y][self.x] == " ":
            self.y += 1

            if self.y >= 0:          # random fall points - do not show until visible
                self.visible = True

            if self.y == len(self.grid) - 2:
                self.symbol = get_gravestone()
                self.dead = True
                self.msgs.append("{} {} {}".format(self.symbol, self.name, get_death_msg(0, self.gender)))
                return True
            return False
        else:
            return True

    def interrupt_if_dead(func):    # is this an appropriate use of a decorator?
        def inner(self, direction, frame):

            if self.dead:
                return 0, 0
            else:
                return func(self, direction, frame)

        return inner

    def end_action(self):
        self.jumping = False
        self.falling = False

    @interrupt_if_dead
    def jump(self, direction, frame):
        x_vel = 1 if direction == "r" else -1

        print(self.x, self.y)


        if self.falling:
            landed = self.fall()
            if not landed:
                return self.frame_speed, frame
            else:
                return self.frame_speed, 0

        elif not self.jumping: # start of jump so populate queue
            self.jumping = True
            self.jump_queue = ([1] * frame) + ([-1] * frame)
            self.frame_speed = FRAME_SPEED / 1.5
            self.y -= 1

        elif self.check_out_of_bounds():
            self.falling = True
        else:

            if len(self.jump_queue):
                y_vel = self.jump_queue.pop(0)

                self.frame_speed += y_vel/300
                #print("Frame speed is {}".format(self.frame_speed))

                self.x += x_vel
                self.y -= y_vel


            elif self.grid[self.y][self.x] != " ":  # jump complete - platform
                return self.frame_speed, 0
            else:
                self.falling = True


        return self.frame_speed, frame







    @interrupt_if_dead
    def move(self, direction, frame):
        # if self.dead:
        #     return 0

        vel = 1 if direction == "r" else -1

        self.frame_speed += 0.01

        if self.check_out_of_bounds(True):
            return self.frame_speed, 0

        if self.grid[self.y+1][self.x] in ["/", "\\"]:
            self.y += 1
        elif self.grid[self.y][self.x] in ["/", "\\"]:
            self.y -= 1
        elif self.grid[self.y][self.x] == "_":
            pass
        else:
            if self.fall():
                return self.frame_speed, 0
            else:
                return self.frame_speed, frame



        self.x += vel
        return self.frame_speed, frame - 1







    def name_pos_check(self, grid_x, grid_y):
        '''Check grid pos against worm pos, return True if name
        of worm should be displayed'''
        if grid_x >= self.x:
            if grid_y == self.y - NAME_DISTANCE:
                return True
        return False

