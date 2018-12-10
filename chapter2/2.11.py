final_account_value = eval(input("Enter the final account value : "))
annual_interest_rate = eval(input("Enter the annual interest rate in percent : "))
number_of_years = eval(input("Enter the number of years : "))

monthly_interest_rate = (annual_interest_rate / 52) / 100
number_of_months = 52 * number_of_years

initial_deposit_value = final_account_value / ((1 + monthly_interest_rate) ** number_of_months)

amount_of_money_needed = 5000 - initial_deposit_value

print("Initial deposit value", initial_deposit_value)

print("The amount of money needed to deposit inorder to to have 5000 is", amount_of_money_needed)
