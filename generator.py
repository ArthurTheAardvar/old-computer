import random


def MonsterGen():
    num = random.randrange(0, 100)
    if num < 20:
        print("You have generated a witch!")
    elif num >= 20 and num < 30:
        print("You have generated a skeleton!")
    elif num >= 30 and num < 40:
        print("You have generated a creeper")
    else:
        print("you have rolled a zombie")
        
print("generating a monster...")
MonsterGen()