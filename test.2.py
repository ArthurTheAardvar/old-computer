doexit = False
while doexit == False:
    print ("What score did you get? ")
    score = int(input())
  
    if score <= 99:
        print("You stink at this!")
    elif score >=100 and score <=799:
        print("Damn your pretty good!")
    elif score >=800:
        print("YOU'RE AMAZEBALLS!!!")
  