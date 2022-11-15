quit = False
while quit == False:
    num = int(input("Press a number that can be multiplied by two: "))
    if num == 0: 
        quit= True
    if num > 0:
        print(num*(2))
    else:
        ("good job you did a simple task!")
        
        
print("goodbye!")