minutes = eval(input("Enter the number of minutes : "))
hours = minutes // 60
days = hours // 24
years = days // 365

print(minutes, "minutes is approximately", years, "and", days, "days")
