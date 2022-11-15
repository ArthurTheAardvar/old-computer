import random
inventory = [" ", " ", " "] #list that holds the inventory

def Floorfall():
    num = random.randrange(0, 100)
    if inventory[0] == "lucky charm":
        if num < 5:
            print("You fell through the floor and died")
            return 1
        elif num <20:
            print("You found a magic door that lets you out!")
            return 2
        else:
            print("The floor creaks ominously")
            return 3
    else:
        if num < 10:
            print("You fell through the floor and died")
            return 1
        elif num <20:
            print("You found a magic door that lets you out!")
            return 2
        else:
            print("The floor creaks ominously")
            return 3
room = 1
doExit = False
while doExit == False:
    if room == 1:
        choice = input("You are in room 1, you can go (e)ast or (w)est")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        elif choice == 'w' or choice == 'W' or choice == 'west':
            room = 3
    if room == 2:
        choice = input("You are in room 2, you can go (w)est or (n)orth")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 1
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 4
    if room == 3:
        choice = input("You are in room 3, you can go (e)ast")
        print("You see a rug on the floor")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 1
        elif choice == "rug" or choice == "look under rug":
            inventory[0] = "lucky charm"
    if room == 4:
        choice = input("You are in room 4, you can go (s)outh")
        result = Floorfall()
        if result == 1:
            doExit = True
            dead = True
        elif result == 2:
            doExit = True
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 2
def dead():        
    if dead == True:
        print("Game Over")
    else:
        print("You won, congrats")