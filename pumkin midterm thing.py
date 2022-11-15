def garden(p):
    print("Your pumpkins are growning!")
    num = 1
    while num <= p:
        print("now you have", num, "pumpkins")
        num+=1
        
seed = int(input("Enter number of seeds planted!"))
garden(seed)
    


