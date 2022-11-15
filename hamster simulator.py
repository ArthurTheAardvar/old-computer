class hamster:
    def __init__(self, name):
        self.name = name
        self.hunger = int(input("How much do you plan to feed Vanessa, Tom and Whiskers in order: "))
        self.mood = "happy"
        self.boredom = 20
    def eat(self):
        self.hunger += 20
    def play(self):
        self.boredom += 20
    def update(self):
        self.hunger -= 10
        self.boredom -= 10
        if self.boredom <0:
            self.mood = "grumpy"
        elif self.boredom <20:
            self.mood = "happy"
        elif self.hunger < 0:
            self.mood = "grumpy"
        elif self.hunger <20:
            self.mood = "happy"
        else:
            self.mood = "ecstatic"
    def printInfo(self):
        print("My name is", self.name, "and I am", self.mood)
    
#------------------------------------------------------------------------
pet1 = hamster("Vanessa")
pet2 = hamster("Tom")
pet3 = hamster("Whiskers")
print("welcome to the hamster simulator")
print()
#game loop##########################################
while True:
    choice = int(input("press 1 to feed Vanessa, 2 to feed Tom, 3 to feed Whiskers, 4 to play with them and 5 to check info"))
    if choice == 1:
        pet1.eat()
    elif choice == 2:
        pet2.eat()
    elif choice == 3:
        pet3.eat()
    elif choice == 4:
        pet1.play()
        pet2.play()
        pet3.play()
    else:
        pet1.printInfo()
        pet2.printInfo()
        pet3.printInfo()
    
    pet1.update()
    pet2.update()
    pet3.update()
#end game loop################################################