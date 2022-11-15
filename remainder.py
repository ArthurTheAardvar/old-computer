#Write a function that takes two integer parameters
#and returns the ramainder when the first parameter is divided by the seocnd.
#Call the function in a pring statement so it prints out the number
a = input("Enter first number")
b = input("Enter second number")
def remainder(a,b):
    return a % b
print(remainder(a,b))