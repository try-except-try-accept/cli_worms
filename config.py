from helpers import create_angles
import platform

if platform.system() == "Windows":
    CLEAR = "CLS"
else:
    CLEAR = "clear"

WORMS_PER_TEAM = 3
HEIGHT = 30
WIDTH = 200
FRAME_SPEED = 0.125
MAX_TEAM_SIGNUP = 3
MIN_TEAM_SIGNUP = 1
NAME_DISTANCE = 3
MIN_GAP_LENGTH = 1
MAX_GAP_LENGTH = 5
INTRO_FRAME_SPEED = 0.5
MESSAGE_QUEUE_FRAME_RATE = 0.5
TEST_MODE = True
GRAVITY = 0.9  # percentage change per frame
ARROW_LIFE = 30 # how many frames does an arrow last before exploding?

STOP_ANIMATION = -1 # flag to signify animation should stop

ORIENTATIONS = ["n", "nne", "ne", "ene", "e", "ese", "se", "sse", "s", "ssw", "sw", "wsw", "w", "wnw", "nw", "nnw"]

ACTIONS = [["left", 1, 30, "to move to the left by a number of characters."],
           ["right", 1, 10, "to move to the left by a number of characters."],
           ["ljump", 1, 10, "to jump leftwards by a specific height."],
           ["rjump", 1, 10, "to jump rightwards by a specific height."],
           ["mine", 1, 30, "to lay a mine for x frames."],
           ["shoot", ORIENTATIONS, None, "to shoot in a certain direction:"]]



ANGLES = create_angles()



D_MAP = [[0, -1, '🡡'],
         [1, -1, '🡥'],
         [1, 0, '🡪'],
         [1, 1, '🡦'],
         [0, 1, '🡣'],
         [-1, 1, '🡧'],
         [-1, 0, '🡨'],
         [-1, -1, '🡤']]


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


EXPLOSIONS = '''☆, ✰, ✯, ✭, ✵, ✪, ⚝'''.split(", ")
