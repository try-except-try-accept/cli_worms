from random import randint, shuffle
from config import *
from time import sleep
from os import system
from helpers import get_airdrop_msg

ENTRY = randint(int(HEIGHT * 0.25), int(HEIGHT * 0.75))

class World:

    def __init__(self, worms, msg_queue, msg_history):
        self.grid = self.create_scenery()
        self.msg_queue = msg_queue # is this weird? am i allowed to pass a list between objects
        self.msg_history = msg_history
        # so everything 'knows about' it ?
        for w in worms:  # is this weird?
            w.grid = self.grid
        shuffle(worms)
        self.worms = worms
        
    def display_msg_history(self):
        print()
        print()
        print("\n".join(self.msg_history[-5:]))

    def display_msg_queue(self):
        while len(self.msg_queue) > 0:
            msg = self.msg_queue.pop(0)
            self.msg_history.append(msg)
            print(msg)
            sleep(1)

    def air_drop(self, start_game=True, dropped_items=None):
                
        if not start_game:
            msg = get_airdrop_msg()
            print(msg)
            sleep(1)
            self.msg_history.append("msg")
            self.msg_history.append("An airdrop was received.")
            countdown = 3

        else:
            countdown = 10
            dropped_items = self.worms

        print("Commencing airdrop in...")
        sleep(1)
        for i in range(countdown, -1, -1):
            print(f" {i}")
            sleep(0.25)
        print("AWAY!")
        sleep(2)
        system(CLEAR)

        grounded = [False] * (WORMS_PER_TEAM * 2)
        while not all(grounded):
            system(CLEAR)
            grounded = [w.fall() for w in dropped_items]
            self.display_scenery()
            self.display_msg_history()
            sleep(FRAME_SPEED)

        system(CLEAR)


    def act(self, worm, action):
        command, action_frame = action.split(" ")
        action_frame = int(action_frame)

        if command in ["left", "right"]:

            while action_frame > 0:
                system(CLEAR)
                action_frame -= 1
                action_frame = worm.move(command, action_frame)
                self.display_scenery()
                self.display_msg_history()
                sleep(FRAME_SPEED)


    def create_scenery(self):
        grid = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]

        y = ENTRY

        draw = 0   # miss out platform chunks if > 0.
        try:
            for x in range(WIDTH):

                if not draw:
                    if randint(0, 1):
                        # go straight
                        grid[y][x] = "_"
                    elif randint(0, 1):
                        # drop down
                        y += 1
                        grid[y][x] = "\\"
                    else:
                        # go up
                        grid[y][x] = "/"
                        y -= 1

                if not randint(0, 6):
                    draw = randint(MIN_GAP_LENGTH, MAX_GAP_LENGTH)

                if draw > 0:
                    draw -= 1

        except:
            pass

        return grid

    def display_scenery(self, current_turn=None):
        if current_turn is not None:
            worm_whose_turn = list(" ↙ " + (current_turn.name.split(" ")[0]))

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):

                if current_turn and current_turn.name_pos_check(x, y) and len(worm_whose_turn):
                    print(worm_whose_turn.pop(0), end="")
                else:
                    for w in self.worms:
                        if w.x == x and w.y == y:
                            print(w.symbol, end="")
                            break
                    else:
                        print(cell, end="")
            print()



