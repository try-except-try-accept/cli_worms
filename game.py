from time import sleep
from json import loads

from helpers import random_name
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
        self.welcome()
        worms = self.create_worms()
        self.world = World(worms)
        self.game_over = False


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
                worms.append(Worm(worm_name, team, start_x, team_symbol))

                x_pos_used.append(start_x)

        return worms

    def main_game_loop(self):
        print("Commencing airdrop in...")
        sleep(1)
        for i in range(10, -1, -1):
            print(f" {i}")
            sleep(0.25)
        print("AWAY!")
        sleep(2)
        system("clear")


        self.world.air_drop()

        for worm in self.world.worms:

            if not worm.dead:

                system("clear")
                self.world.display_scenery(worm)
                print()
                print(f"It's {worm.name}'s turn ({worm.team})")

                input()
                action = self.turn_menu()
                self.world.act(worm, action)













