import winsound
import math
import easygui


choice = 2
while choice != 0:
    choice = int(input("press 1 to add, 2 to subtract, 3 to multiply, 4 to divide, 5 to square root, 6 to another way to square root, 7 to use sin on a number, 8 to power a number by an exponent"))
    if choice ==1:
        num1 = int(input("please enter first number to add: "))
        num2 = int(input("please enter second number: "))
        print (num1, " + ", num2, " = ", num1+num2)
        winsound.Beep(100,300)                   
    if choice == 2:
        num2 = int(input("please enter first number to subtract: "))
        num3 = int(input("please enter second number: "))
        print (num3, " - ", num4, " = ", num3-num4)
        winsound.Beep(200,300)
    if choice == 3:
        num5 = int(input("please enter first number to multiply: "))
        num6 = int(input("please enter second number: "))
        print (num5, " * ", num6, " = ", num5*num6)
        winsound.Beep(300,300)
        
    if choice == 4:
        num7 = int(input("please enter first number to divide: "))
        num8 = int(input("please enter second number: "))
        print (num7, " / ", num8, " = ", num7/num8)
        winsound.Beep(400,300)
        
    if choice == 5:
        num9 = int(input("please enter first number to power by: "))
        num10 = int(input("please enter second number"))
        print (num9, " ** ", num10 , " = ", num9**num10)
        winsound.Beep(500,300)
    if choice == 6:
        num11 = int(input("please enter first number to square root: "))
        num11 = math.sqrt(num11)
        print(num11)
        winsound.Beep(600,300)
    if choice == 7:
        num12 = int(input("please enter first number to use sin on: "))
        num12 = math.sin(math.pi)
        print(num12)
        
    if choice == 8:
        num13 = int(input("please enter first number to use cosine on: "))
        num13 = math.cos(num13)
        print(num13)
        winsound.Beep(700,300)
    
        
    
    elif choice == 0:
        print("goodbye")
        easygui.msgbox("Goodbye", title="CYA")

    else:
        print("Not an option")
        

        
    
        