import random 

def monster(biome):
    num = random.randrange(0, 100)
    if biome == "dungeon":
        if num < 20:
            print("A zombie attacks you")
        elif num <60:
            print("A skeleton shoots an arrow at you!")
        elif num <90:
            print("A spider crawls towards you")
        else:
            ("A witch throws a potion at you!")
    elif biome == "desert":
        if num < 20:
            print("A zombie attacks you")
        elif num <30:
            print("A skeleton shoots an arrow at you!")
        elif num <60:
            print("A spider crawls towards you")
        else:
            ("A witch throws a potion at you!")
    elif biome == "Abandoned City":
        if num < 25:
            print("An infected human appears")
        elif num < 75:
            print("An infected dog runs towards you")
        elif num < 85:
            print("A bear appears before you")
        elif num < 100:
            print("You face a hostile human")

print("You wake up in a creepy house.")
room = 1
while True:
    if room == 1:
        print("You are in room 1, you can go (e)ast")
        choice = input()
        if choice == 'e' or  choice == 'E' or  choice == 'east' or choice == 'East':
            room = 2
            
    if room == 2:
        monster("dungeon")
        print("You are in room 2, you can go (s)outh or (w)est")
        choice = input()
        if choice == 's' or  choice == 'S' or  choice == 'south' or choice == 'South':
            room = 3
        elif choice == 'w' or choice == 'W' or choice == 'west' or choice == 'West':
            room = 1
            
    if room == 3:
        monster("Abandoned City")
        print("You are in room 3, you can go (s)outh or (n)orth")
        choice = input()
        if choice == 's' or  choice == 'S' or  choice == 'south' or choice == 'South':
            room = 4
        elif choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 2
            
    if room == 4:
        monster("desert")
        print("You are in room 4, you can go (s)outh or (n)orth")
        choice = input()
        if choice == 'n' or choice == 'N' or choice == 'north' or choice == 'North':
            room = 3