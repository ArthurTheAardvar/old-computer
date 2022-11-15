inventory = ["Stone Sword"]
room=1
doExit = False
while doExit == False:
    print("Your inventory: ", end = " ")
    print(inventory)
    if room == 1:
        choice = input("You are in room 1, you can go (e)ast")
        print("You have find a health potion and silver sword")
        inventory.append("Health potion")
        inventory.append("Silver Sword")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
    if room == 2:
        choice = input("You are in room 2, you can go (w)est or (s)outh, you notice a rug on the floor")
        if choice == "rug" or choice == "look under rug":
            print("You found a key")
            inventory.append("key")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 1
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 3
    if room == 3:
        choice = input("You are in room 3, you can go (n)orth or (s)outh")
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 2
        elif choice == 's' or choice == 'S' or choice == 'south':
            key = False
            for i in range(len(inventory)):
                if inventory[i] == key:
                    key = True
            if key == True:
                print("You opened the door with the key")
                room = 4
            else:
                print("The door is locked")
    if room == 4:
        choice = input("You are in room 4, you can go (n)orth")
        print("A dragon appears for some reason")
        if inventory[0] == "Stone Sword":
            print("The dragon breathes fire on your sword and it turns into lava. You died")
            doExit = True
        elif inventory[0] == "silver sword":
            print("You slay the dragon")
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 3