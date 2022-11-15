import time #bring in files of prewritten code
import random

#function Definitions-------------------------------------------------------------------------------------
def TimeKeygame():
    count = 0 #declaring and initializing variables
    tooSlow = False
    while count < 5 and tooSlow == False: #game loop
        num = random.randrange(0,10) #random number between 0-9
        TimeStart = time.perf_counter()#start a timer
        print("press the number", num)
        userNum = int(input())
        TimeEnd = time.perf_counter()
        if TimeEnd-TimeStart <2 and userNum == num:
            print("Good job")
            count+=1
        else:
            if userNum!=num:
                print("Wrong Number")
            else:
                print("TOO SLOW")
            tooSlow = True
            
    if tooSlow == False:
        print("You have FAILED!")
        return False
    else:
        print("You have completed the task")
            
#end function defenitions----------------------------------------------------------------------------------

task1 = TimeKeygame()

#while task1 == False and task2 == False and task3 == False: #main game loop