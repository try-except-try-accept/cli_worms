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


            if not randint(0, 2):
                name = name
            elif randint(0, 1):
                name += " The " + rand_choice(NOUNS).title()
            else:
                name = rand_choice(ADJECTIVES) + " " + name

    else:


        noun_needed = False
        if randint(0, 2):
            name = rand_choice(ADJECTIVES)
        elif randint(0, 1):
            name = rand_choice(NOUNS)
        else:
            name = rand_choice(rand_choice(NAMES).split()) + "'s"
            if not randint(0, 3):
                name += " " + rand_choice(ADJECTIVES)
                noun_needed = True


        if randint(0, 1) and not noun_needed:
            name += " " + rand_choice(ADJECTIVES)


        name += " " + rand_choice(NOUNS)

        if name[-1] != "s" and randint(0, 1):
            name += "s"


    return name.title().replace("  ", " ").replace("'S", "'s")