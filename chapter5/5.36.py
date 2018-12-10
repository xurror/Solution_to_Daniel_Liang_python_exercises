#Program to implement 
import random
count = 0

print("Rules: scissor (0), rock (1), paper (2) ")
while count <= 2 or count <= -2:
    num = random.randint(0, 2) 
    user = eval(input("Enter your choice: "))

    # Check the User Guess with Computer's Guess
    if num == 0:
        if user == 0:
            print("It is a draw")
        elif user == 1: 
            print("You won!")
            count += 1       
        elif user == 2:
            print("Computer won!")
            count -= 1
    elif num == 1:
        if user == 0:
            print("Computer won!")
            count -= 1
        elif user == 1:
            print("It is a draw")
        elif user == 2:
            print("You won!")
            count += 1
    elif num == 2:
        if user == 0:
            print("You won!")
            count += 1       
        elif user == 1:
            print("Computer won!")
            count -= 1
        elif user == 2: 
            print("It is a draw")

if count > 2: 
    print("You won more than two times continuously")
else:
    print("The computer won more than two times continously")

