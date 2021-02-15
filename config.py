import platform

if platform.system() == "Windows":
    CLEAR = "CLS"
else:
    CLEAR = "clear"

WORMS_PER_TEAM = 2
HEIGHT = 30
WIDTH = 200
FRAME_SPEED = 0.125
MAX_TEAM_SIGNUP = 0
MIN_TEAM_SIGNUP = 0
NAME_DISTANCE = 1
MIN_GAP_LENGTH = 0
MAX_GAP_LENGTH = 0
INTRO_FRAME_SPEED = 0.1




ACTIONS = [["left", 1, 30, "to move to the left by a number of characters."],
           ["right", 1, 10, "to move to the left by a number of characters."],
           ["ljump", 1, 10, "to jump leftwards by a specific height."],
           ["rjump", 1, 10, "to jump rightwards by a specific height."]]



