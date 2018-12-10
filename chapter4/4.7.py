# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))
# Convert the amount to cents
remainingAmount = int(amount * 100)
# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25
# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10
# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5
# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount
#Display the results
if numberOfOneDollars <= 1:
    print("Your amount", amount, "consists of", numberOfOneDollars, "dollar")
else:
    print("Your amount", amount, "consists of", numberOfOneDollars, "dollars")

if numberOfQuarters <= 1:
    print("Your amount", amount, "consists of", numberOfQuarters, "quarter")
else:
    print("Your amount", amount, "consists of", numberOfQuarters, "quarters")

if numberOfDimes <= 1:
    print("Your amount", amount, "consists of", numberOfDimes, "dime")
else:
    print("Your amount", amount, "consists of", numberOfDimes, "dimes")

if numberOfNickels <= 1:
    print("Your amount", amount, "consists of", numberOfNickels, "nickel")
else:
    print("Your amount", amount, "consists of", numberOfNickels, "nickels")

if numberOfPennies <= 1:
    print("Your amount", amount, "consists of", numberOfPennies, "penny")
else:
    print("Your amount", amount, "consists of", numberOfPennies, "pennies")
'''print("Your amount", amount, "consists of\n",
"\t", numberOfOneDollars, "dollars\n",
"\t", numberOfQuarters, "quarters\n",
"\t", numberOfDimes, "dimes\n",
"\t", numberOfNickels, "nickels\n",
"\t", numberOfPennies, "pennies")
'''
