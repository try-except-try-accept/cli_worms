import platform

if platform.system() == "Windows":
    CLEAR = "CLS"
else:
    CLEAR = "clear"

WORMS_PER_TEAM = 8
HEIGHT = 30
WIDTH = 200
FRAME_SPEED = 0.125
MAX_TEAM_SIGNUP = 0
MIN_TEAM_SIGNUP = 0
NAME_DISTANCE = 3
MIN_GAP_LENGTH = 0
MAX_GAP_LENGTH = 0
INTRO_FRAME_SPEED = 0
TEST_MODE = True

ACTIONS = [["left", 1, 30, "to move to the left by a number of characters."],
           ["right", 1, 10, "to move to the left by a number of characters."],
           ["ljump", 1, 10, "to jump leftwards by a specific height."],
           ["rjump", 1, 10, "to jump rightwards by a specific height."]]



CONFIG_MSGS = {

"input_or_generate":"""Enter any key to set team and worm names
Leave blank to randomly generate.
""",


              }

LOGO = """   ______  _____     _____      ____      ____   ___   _______     ____    ____   ______   
 .' ___  ||_   _|   |_   _|    |_  _|    |_  _|.'   `.|_   __ \   |_   \  /   _|.' ____ \  
/ .'   \_|  | |       | |        \ \  /\  / / /  .-.  \ | |__) |    |   \/   |  | (___ \_| 
| |         | |   _   | |         \ \/  \/ /  | |   | | |  __ /     | |\  /| |   _.____`.  
\ `.___.'\ _| |__/ | _| |_         \  /\  /   \  `-'  /_| |  \ \_  _| |_\/_| |_ | \____) | 
 `.____ .'|________||_____|         \/  \/     `.___.'|____| |___||_____||_____| \______.' """



