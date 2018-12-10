# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

realAmount = (int(amount % 100) / 100)+ int(amount // 100)
# Convert the amount to cents
remainingAmount = int(realAmount * 100)

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

# Display the results
print("Your amount", abs(amount), "consists of\n",
"\t", abs(numberOfOneDollars), "dollars\n",
"\t", abs(numberOfQuarters), "quarters\n",
"\t", abs(numberOfDimes), "dimes\n",
"\t", abs(numberOfNickels), "nickels\n",
"\t", abs(numberOfPennies), "pennies")
#print(realAmount)