import random

#------------------------------------------------------------------------
def BattleSystem(monsterType, playerHealth):
    if monsterType == "Creeper":
        monsterHealth = 20
        print("A creeper approaches")
    elif monsterType == "Skeleton":
        monsterHealth = 40
        print("A skeleton shoots at you")
        int("The", monsterType, "attack for", monsterAttack)
        playerHealth = playerHealth-monsterAttack
        print("Your health is now", playerHealth)
        
        playerAttack = random.randrange(25, 35)
        print("You attack for", playerAttack)
        monsterHealth = monsterHealth-playerAttack
        print("The monster's health is now", monsterHealth)
        
        
    if monsterHealth<0:
        print("You have defeated the",monsterType)
    else:
        print("You have been defeated by", monsterType)
        
        return playerHealth
        
        
#------------------------------------------------------------------------        
       
BattleSystem("Skeleton", 100)
        
    
while monsterHealth>0 and playerHealth >0:
    if monsterType == "Creeper":
        monsterAttack = random.randrange(20, 30)
    elif monsterType == "Skeleton":
        monsterAttack = random.randrange(10, 16)
    print("The", monsterType, "attack for", monsterAttack)
    playerHealth = playerHealth-monsterAttack
    print("Your health is now", playerHealth)
        
    playerAttack = random.randrange(25, 35)
    print("You attack for", playerAttack)
    monsterHealth = monsterHealth-playerAttack
    print("The monster's health is now", monsterHealth)
        
        
    if monsterHealth<0:
        print("You have defeated the",monsterType)
    else:
        print("You have been defeated by", monsterType)
        
        return playerHealth
        
        
#------------------------------------------------------------------------        
       
BattleSystem("Skeleton", 100)
        
    