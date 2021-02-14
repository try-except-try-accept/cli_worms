from time import sleep
from json import loads

from helpers import random_name, get_losing_team_msg
from world import World

from worm import Worm

from os import system
from random import randint

from config import *

CONFIG_MSG = {

"input_or_generate":"""Enter any key to set team and worm names
Leave blank to randomly generate.
""",


              }

class Game:

    def __init__(self):
        self.message_queue = []
        self.welcome()
        self.teams = {}
        worms = self.create_worms()
        self.world = World(worms)
        self.game_over = False


    def check_end_game(self):
        for team, worms in self.teams.items():
            if all([w.dead for w in worms]):
                self.message_queue.append("{} {}".format(team, get_losing_team_msg()))
                return True
        return False

    def welcome(self):
        print("""   ______  _____     _____      ____      ____   ___   _______     ____    ____   ______   
 .' ___  ||_   _|   |_   _|    |_  _|    |_  _|.'   `.|_   __ \   |_   \  /   _|.' ____ \  
/ .'   \_|  | |       | |        \ \  /\  / / /  .-.  \ | |__) |    |   \/   |  | (___ \_| 
| |         | |   _   | |         \ \/  \/ /  | |   | | |  __ /     | |\  /| |   _.____`.  
\ `.___.'\ _| |__/ | _| |_         \  /\  /   \  `-'  /_| |  \ \_  _| |_\/_| |_ | \____) | 
 `.____ .'|________||_____|         \/  \/     `.___.'|____| |___||_____||_____| \______.' """)

    def create_worms(self):
        gen = False
        if not input(CONFIG_MSG["input_or_generate"]):
            gen = True

        worms = []
        p = 0
        for team_symbol in ["S", "Ƨ"]:
            p += 1
            if gen:
                team = random_name()
            else:
                print(f"Player {p} ({team_symbol}) --- enter team name:\n\n")
                team = input()
                while len(team) < 4:
                    team = input("No - please give a team name: ")

            print("""
            
Player {} --- your team will be named:
            
{}
""".format(p, team.upper()))
            self.teams[team] = []
            sleep(1)

            for i in range(1, WORMS_PER_TEAM + 1):
                if gen:
                    worm_name = random_name(True)
                else:
                    print(f"Player {p} --- enter name for worm {i}:\n\n")
                    worm_name = input()
                    while len(worm_name) < 4:
                        worm_name = input("No - please give a worm name: ")

                print("{0} joined {1}!!!".format(worm_name.upper(), team))
                sleep(randint(1, TEAM_WAIT_TIME))

                x_pos_used = []

                start_x = randint(0, WIDTH)

                while start_x in x_pos_used:
                    start_x = randint(0, WIDTH)
                new_worm = Worm(worm_name, team, start_x, team_symbol, self.message_queue)
                worms.append(new_worm)
                self.teams[team].append(new_worm)
                x_pos_used.append(start_x)

        return worms

    def action_help(self):
        print("")
        for a, min_, max_, exp in ACTIONS:
            print(f"   - Type {a} x to {exp}. Minimum value for x is {min_}, maximum is {max_}.")
        print()

    def validate_action(self, command):
        if command == "help":
            return self.action_help()
        try:
            cmd, param = command.split(" ")
        except:
            return False
        for a, min_, max_, exp in ACTIONS:
            if cmd == a:
                if param.isdigit():
                    param = int(param)
                    if param >= min_ and param <= max_:
                        return True

        return False


    def main_game_loop(self):
        print("Commencing airdrop in...")
        sleep(1)
        for i in range(10, -1, -1):
            print(f" {i}")
            sleep(0.25)
        print("AWAY!")
        sleep(2)
        system(CLEAR)

        self.world.air_drop()
        game_over = False
        while not game_over:

            for worm in self.world.worms:

                game_over = self.check_end_game()

                print()
                print()
                while len(self.message_queue):
                    print(self.message_queue.pop(0))
                    sleep(2)
                print()
                sleep(1)
                system(CLEAR)


                if game_over:
                    break

                if not worm.dead:

                    self.world.display_scenery(worm)

                    print(f"It's {worm.name}'s turn ({worm.team})")

                    action = input("Enter a command or type HELP for guidance! ")
                    while not self.validate_action(action):
                        action = input("Enter a command: ")

                    self.world.act(worm, action)












