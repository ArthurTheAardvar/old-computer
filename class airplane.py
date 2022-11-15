class Airplane:
    def __init__(self, type):
        self.type = type
        self.speed = 0
        self.is_in_air = False
        self.fuel = 5000
        
    def printPlane(self):
        print("Hi, I'm a", self.type, ".")
        if self.is_in_air == False:
            print("i am on the ground")
        else:
            print("I am in the air")
        print("My speed is ", self.speed, "and my fuel is", self.fuel)
        print()
        
    def fly(self, distance):
        print("Flyiiing")
        self.fuel -= distance
        
a1 = Airplane("F22 Raptor")
a2 = Airplane("Curtiss P-40E Warhawk")
trogdor = Airplane("Boeing 747-8")

a1.fly(200)
a1.printPlane()

a2.fly(200)
a2.printPlane()

trogdor.fly(200)
trogdor.printPlane()
        
        
