Loan = eval(input("Loan Amount: "))
Years = eval(input("Number of Years: "))
rate = 5.00

print("Interest Rate \t Monthly Payment \t Total Payment")

while rate <= 8:

    monthlyPayment = Loan * rate / (1 - 1 / (1 + rate) ** (Years * 12))
    totalPayment = monthlyPayment * Years * 12

    print(str(format(rate, ".3f")) + "%\t\t"
          + str(format(monthlyPayment, ".2f")) + "\t\t"
          + str(format(totalPayment, ".2f")))
    rate += 1 / 8
    
