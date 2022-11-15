import random



def npc(lugar):
    num = random.randrange(0, 100)
    if lugar == "Town":
        if num < 20:
            print("Hey, I like shorts!")
        elif num <30:
            print("Science isn't about why, it's about why not!")
        elif num <45:
            print ("DO A BARREL ROLL!")
        elif num <80:
            print("What is a man? A miserable little pile of secrets.")
        else:
            print("I used to be an adventurer like you. Then I took an arrow in the knee")
            

room = 1
if room == 1:
    print("You wake up, your head dizzy but you see an entity standing infront of you it looks... weird almost like a shadow with multiple faces speak to it?")
    choice = input()
    if choice == 'y' or  choice == 'Y' or  choice == 'yes' or choice == 'YES':
        room = 1
    elif choice == 'n' or choice == 'N':
        print("It grew impatient of you and devoured you")
    else:
        print("What did you expect")
room = 2          
if room == 2:
    npc("Town")
    print(("Would you like to speak to him again?"))
    choice = input()
    if choice == 'y' or  choice == 'Y' or  choice == 'yes' or choice == 'YES':
        room = 2
    elif choice == 'n' or choice == 'N':
        print("It grew impatient of you and devoured you")
    else:
        print("Again what did you expect")

    
   
