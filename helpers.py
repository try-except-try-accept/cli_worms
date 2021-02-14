from json import loads

from random import randint, choice as rand_choice

with open("assets/json/words.json") as f:
    file = loads(f.read())
    NOUNS, ADJECTIVES, NAMES = file['nouns'], file['adjectives'], file['names']

def random_name(worm_name=False):
    name = ""
    if worm_name:

        if not randint(0, 5):
            name = rand_choice('Dr.,Mr.,Miss,Master,Ms.,Mrs.General,Sergeant,Commander,Lieutenant,Corporal,Chancellor,Prime Minister,President'.split(',')) + " "

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