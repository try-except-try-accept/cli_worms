
from config import *
from helpers import get_death_msg, get_gravestone, get_boundary_msg
from random import randint, choice as rand_choice
from sprite import Sprite

class Worm(Sprite):
    def __init__(self, name, team, start_x, symbol, msg_queue):
        x = start_x
        y = randint(-WORMS_PER_TEAM, 0)
        super().__init__(x, y, symbol, False)

        self.msgs = msg_queue
        self.name = name
        self.team = team
        self.dead = False
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

    def out_of_bounds_msg(self):
        self.msgs.append(get_boundary_msg(self.name, self.gender))

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
        vel = 1 if direction == "r" else -1

        self.frame_speed += 0.01

        # if self.check_out_of_bounds(True):
        #     return self.frame_speed, 0

        if vel == -1 and self.grid[self.y][self.x] == "\\":
             self.y -= 1
        elif vel == 1 and self.grid[self.y][self.x] == "/":
             self.y -= 1

        self.x += vel
        if self.check_out_of_bounds(resultant_action=self.out_of_bounds_msg):
            return self.frame_speed, 0

        self.fall()

        return self.frame_speed, frame - 1

    def name_pos_check(self, grid_x, grid_y):
        '''Check grid pos against worm pos, return True if name
        of worm should be displayed'''
        if grid_x >= self.x:
            if grid_y == self.y - NAME_DISTANCE:
                return True
        return False

