from json import loads

from random import randint, choice as rand_choice

with open("assets/json/words.json") as f:
    file = loads(f.read())
    NOUNS, ADJECTIVES, NAMES = file['nouns'], file['adjectives'], file['names']

with open("assets/txt/gravestones.txt", encoding="utf-8") as f:
    GRAVESTONES = [line.strip() for line in f]

def get_gravestone():
    return rand_choice(GRAVESTONES)


def get_death_msg(cause):

    death_messages = ["""sunk to the bottom of the sea.
died a salty death!
was eaten by sharks.
was fed to the fishes.
sunk like an anchor!
drowned their sorrows.
went for a swim!""".split("\n")]

    return rand_choice(death_messages[cause])

def get_airdrop_msg():
    msgs = '''Gifts from the sky!
And the heavens opened!
Reinforcements!!!'''.split('\n')

    return rand_choice(msgs)

def get_boundary_msg(w):
    gender_belong = rand_choice(["himself", "herself"])
    msgs = '''{0} tried to escape!
{0} made a run for it!
... and the end of the world was reached by {0}.
{0} hit a brick wall!
{0} found {1} in the Truman Show...
No surrender, no departure {0}!'''.format(w, gender_belong).split("\n")

    return rand_choice(msgs)


def get_losing_team_msg():
    msgs = '''was wiped off the face of the earth!
was annihilated!
disappeared from the battlefield.
got obliterated!
had no soldiers left...
faced armageddon!!
had no one left standing.'''.split('\n')

    return rand_choice(msgs)


def random_name(worm_name=False):
    name = ""
    if worm_name:

        if not randint(0, 5):
            name = rand_choice('Dr.,Mr.,Miss,Master,Ms.,Mrs.,General,Sergeant,Commander,Lieutenant,Corporal,Chancellor,Prime Minister,President'.split(',')) + " "

        if not randint(0, 3):
            name += rand_choice(NAMES)
        else:
            name += rand_choice(rand_choice(NAMES).split())


            if not randint(0, 5):
                name += str(randint(11, 999))
            elif not randint(0, 2):
                name = name
            elif randint(0, 1):
                name += " The " + rand_choice(NOUNS).title()
            else:
                name = rand_choice(ADJECTIVES) + " " + name

    else:


        noun_needed = False
        article = False
        if randint(0, 2):
            name = rand_choice(ADJECTIVES)
        elif randint(0, 1):
            name = rand_choice(NOUNS)
        elif randint(0, 1):
            name = rand_choice(rand_choice(NAMES).split()) + "'s"
            if not randint(0, 3):
                name += " " + rand_choice(ADJECTIVES)
                noun_needed = True
        else:
            name = rand_choice("The,Those,Some,We,Us,Team,Council of,The,Three".split("\n"))
            article = True


        if randint(0, 1) and not noun_needed:
            name += " " + rand_choice(ADJECTIVES)


        name += " " + rand_choice(NOUNS)

        if name[-1] != "s" and randint(0, 1) and not article:
            name += "s"

        if article:
            if name[-1] not in "aeiou":
                name += rand_choice("tes,cies,ts,ps,x,z".split("\n"))
            else:
                if not randint(0, 2):
                    name += name[-1] + rand_choice("y,o,a,ee,ox".split("\n"))




    return name.title().replace("  ", " ").replace("'S", "'s")