import random
import math

inventory = ["empty", "empty", "empty", "empty", "empty"]
inventory[random.randrange(0, 5)]


def annoying():
    inven=random.randrange(0, 100)
    
    if inven<= 25:
        inventory[random.randrange(0, 5)] = "book"
    elif inven <=40:
        inventory[random.randrange(0, 5)] = "frog"
    elif inven <=80 :
        inventory[random.randrange(0, 5)] = "potion"
    else:
        inventory[random.randrange(0, 5)] = "cupcake"
        

    print(inventory)


annoying()
annoying()
annoying()
annoying()
annoying()