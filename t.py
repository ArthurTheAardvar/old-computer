import random


while True:
    def NPC(Place):
        num = random.randrange(0, 100)
    if Place == "Town":
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
while True:
    if room == 1:
        print("You wake up, your head dizzy but you hear someone speaking to you, Listen?")
        choice = input()
        if choice == 'y' or  choice == 'Y' or  choice == 'yes' or choice == 'YES':
            room = 2
        elif choice == 'n' or choice == 'N':
            room = 3
        else:
            print("What did you expect")
            
    if room == 2:
        NPC("Town")
        
        print(("Would you like to speak to him again?"))
        choice = input()
        if choice == 'y' or  choice == 'Y' or  choice == 'yes' or choice == 'YES':
            room = 2
        elif choice == 'n' or choice == 'N':
            room = 3
