birth_in_7_sec = 1
birth_per_hour = 3600 // 7
birth_per_day = 24 * birth_per_hour

immigrants_in_45_sec = 1
immigrants_per_hour = 3600 // 45
immigrants_per_day = 24 * immigrants_per_hour

death_in_13_sec = 1
deaths_per_hour = 3600 // 13
deaths_per_day = 24 * deaths_per_hour

total_pop_per_day = birth_per_day + immigrants_per_day - deaths_per_day
total_pop =312032486 + 365 * total_pop_per_day
years = eval(input("Enter the number of years : "))
b = 1
a = total_pop
while b < (years + 1):
    
    print("total population in year", years, "is =", a)
    b += 1
    a += total_pop
