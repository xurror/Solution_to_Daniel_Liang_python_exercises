import math

print("number \t Square Root")
number = 0

for number in range(0, 21, 2):
    print(str(number)
          + str(format(math.sqrt(number), "15.4f")))
          
