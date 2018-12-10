import random

number1, number2 = random.randint(0, 99), random.randint(0, 99)
answer = eval(input("What is the sum of " + str(number1) + " and " + str(number2) + " : "))


print("The sum", number1, "+", number2, "=", answer, "is", number1 + number2 == answer)
