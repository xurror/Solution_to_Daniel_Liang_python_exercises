annual_interest_rate = eval(input('Enter annual interest rate : '))
monthly_saving = eval(input("Enter monthly saving amount : "))

monthly_interest_rate = (annual_interest_rate / 100) / 12

first_month = 100 * (1 + 0.00417)

months = 0

while months < 5:

    next_month = (100 + first_month) * (1 + 0.00417)

    first_month = next_month

    months += 1

print("After the sixth month the account saving is", first_month)
