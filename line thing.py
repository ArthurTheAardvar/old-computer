import time
import random

n1 = random.randrange(0, 100)
n2 = random.randrange(0, 100)
n3 = random.randrange(0, 100)
n4 = random.randrange(0, 100)
print("Type the numbers in order:",n1, n2, n3, n4,"(press enter after each number)")
TimeStart = time.perf_counter()
num1 = input()
num2 = input()
num3 = input()
num4 = input()
TimeEnd = time.perf_counter()
print(f"That took you in {TimeEnd-TimeStart:0.4f} seconds")
if TimeEnd-TimeStart <10:
    print("Good Job!")
else:
    print("WAYYYY TO SLOW")