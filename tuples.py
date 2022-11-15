#tuples are variables that store multiple variables, help you shorten your code
colors = (200,150,50) #a tuple

print(colors[0])
print(colors[1])

print(colors)

#find the average of the numbers
sum = 0
for i in colors:
    sum+=i
    
average = sum/(len(colors))
print("The average is", average)