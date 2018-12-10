import random
x = random.randint(0, 1)

guess = eval(input("Enter \"1\" for a \"HEAD\" and \"0\" for a \"TAIL\": "))
if guess == x:
    print("Correct, right pick")
else:
    print("Oops, wrong")
