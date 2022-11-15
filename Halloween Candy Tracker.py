import random


ButterFingers = 0
Hersheys = 1
PeanutButterCups = 2
MandMs = 3
SourPatchKids = 4
Rocks = 0

inventory = [ButterFingers, Hersheys, PeanutButterCups, MandMs, SourPatchKids, Rocks]



def Candies():
    TeethareGone = random.randrange(0, 100)
    candy =random.randrange(1, 4)
    
    if TeethareGone<= 15:
        inventory[0] += candy
    elif TeethareGone <=35:
        inventory[1] += candy
    elif TeethareGone <=70 :
        inventory[2] += candy
    elif TeethareGone <=80:
        inventory[3] += candy
    elif TeethareGone <=98:
        inventory[4] += candy
    else:
        inventory[5] += candy
    
        
    


Candies()
Candies()
Candies()
Candies()
Candies()

print("You got", inventory[0],"Butterfinger Bars")
print("You got", inventory[1],"Hershey Bars")
print("You got", inventory[2],"Peanut Butter Cups")
print("You got", inventory[3],"M&Ms")
print("You got", inventory[4],"Sour PatchKids!")
print("You got", inventory[5],"Rocks")
print("Your total candy count for each kind is:", inventory)