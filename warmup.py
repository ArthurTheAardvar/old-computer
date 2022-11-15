age = int(input("What's your age?: "))

if age <= 13:
    print("You are too young to play...")
elif age > 13 and age <= 17:
    print("You have one shot at this")
elif age == 42:
    print("You'll embarass the youngsters")
else:
    print("Welcome to the game you can either play in regular or 8-bit mode if you prefer something more nostalgic")

