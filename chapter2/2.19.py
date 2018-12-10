investmentAmount = eval(input("Enter investment amount : "))
annualInterestRate = eval(input("Enter annual interest rate : "))
number_of_years = eval(input("Enter number of years : "))

monthlyInterestRate = (annualInterestRate) / 100
number_of_months = number_of_years

futureInvestmentAmount = investmentAmount * ((1 + monthlyInterestRate) ** number_of_months)

print("Accumulated value is", futureInvestmentAmount)
