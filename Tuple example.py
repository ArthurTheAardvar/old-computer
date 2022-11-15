Friend = ("Alex", "Marco", "Adrian", "Liam", "Nate", "Lupe") #tuple
ages = []
print(Friend)
friend = int(input("What is the age for friend 0: "))
ages.append(friend)
friend = int(input("What is the age for friend 1: "))
ages.append(friend)
friend = int(input("What is the age for friend 2: "))
ages.append(friend)
friend = int(input("What is the age for friend 3: "))
ages.append(friend)
friend = int(input("What is the age for friend 4: "))
ages.append(friend)
friend = int(input("What is the age for friend 5: "))
ages.append(friend)
print(Friend[0], "is", ages[0])
print(Friend[1], "is", ages[1])
print(Friend[2], "is", ages[2])
print(Friend[3], "is", ages[3])
print(Friend[4], "is", ages[4])
print(Friend[5], "is", ages[5])
sum = 0
for i in ages:
    sum+=i
average = sum/(len(ages))
print("The average is", average)