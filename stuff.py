doexit = False
while doexit == False:
    print ("How old are you?")
    age = int(input())
    print("Welcome to the game:" , age)
  
    if age >= 18:
          doexit = True
    elif age <=17 and age >=13:
        print("You'1ll need parental permission to access game")
    elif age <=12 and age >=1:
        print("You're too young for this game")
  