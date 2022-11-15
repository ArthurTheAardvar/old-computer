inventory = ["Rusted Sword"]
room=1
doExit = False
while doExit == False:
    print("Your inventory: ", end = " ")
    print(inventory)

    if room == 1:
        choice = input("You wake up in a strange dungeon, you then stand up and look around and see a rusted sword and a door to the south")
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 2
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 999
            
        if room == 999:
            print("You walked through the wall but at what cost now your falling down an endless void")# or is it
            doExit = True
    
    #room 2----------------
    if room == 2:
        choice = input("You walk through the door and see a chest")
        
        if choice == 'chest':
            print("You found a key")
            inventory.append("key")
        if choice == 'w' or choice == 'W'or choice == 'west':
            room = 3
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 1
        
    if room == 3:
        choice == input("As you walked through the door you see a mirror along with another door to the west")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 4
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 2
        elif choice == "look at mirror":
            print("You see yourself in the reflection, you're bruised and scratched")

    if room == 4:
        choice = input("You walk into the next room noticing a door with red lock")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 3
        elif choice == 's' or choice == 's' or choice == 'south':
            key = False
            for i in range(len(inventory)):
                if inventory[i] == key:
                    key = True
            if key == True:
                print("You opened the door with the key")
                room = 5
            else:
                print("The door is locked")
         
    if room == 5:
        choice = input("You're in room 5 would you like to go south or north?")
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 6
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 4
 
                
    if room == 6:
        choice = input("You're in room 6 would you like to go south or east?")
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 5
        elif choice == 's' or choice == 'S' or choice == 'south':
            room = 7

                
    if room == 7:
        choice = input("You're in room 7 would you like to go north or east?")
        if choice == 'n' or choice == 'N' or choice == 'north':
            room = 6
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 8

                
    if room == 8:
        choice = input("You're in room 8 would you like to go west or east?")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 7
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 9
  
                
    if room == 9:
        choice = input("You're in room 9 would you like to go west or east?")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 8
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 10
 
        
    if room == 10:
        choice = input("You're in room 10 would you like to go west or east?")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 9
        elif choice == 'e' or choice == 'E' or choice == 'east':
            room = 11
     
                
    if room == 11:
        choice = input("You're in room 11 would you like to go north or east?")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 10
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 12
  
                
    if room == 12:
        choice = input("You're in room 12 would you like to go south or east?")
        if choice == 'w' or choice == 'W' or choice == 'west':
            room = 11
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 13
    
                
    if room == 13:
        choice = input("You're in room 13 would you like to go south or east?")
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 12
        elif choice == 'n' or choice == 'N' or choice == 'north':
            room = 14
    
                
    if room == 14:
        choice = input("You're in room 14 would you like to go south or east?")
        if choice == 's' or choice == 'S' or choice == 'south':
            room = 13
        elif choice == 'w' or choice == 'W' or choice == 'west':
            room = 15

                
    if room == 15:
        choice = input("You're in room 15 would you like to go south or east?")
        if choice == 'e' or choice == 'E' or choice == 'east':
            room = 14
    
                
    
