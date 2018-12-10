year = eval(input("Enter year: "))
m = eval(input("Enter month 1-12: "))
q = eval(input("Enter the day of the month 1-31: "))

Monday = 'Monday'
Tuesday = 'Tuesday'
Wednesday = 'Wednesday'
Thursday = 'Thursday'
Friday = 'Friday'
Saturday = 'Saturday'
Sunday = 'Sunday'

#futureDay = today + elapsedDays

k = year % 100
j = year / 100

h = (q + (((26 * (m + 1))) / 10)
     + k + (k // 4)
     + (j // 4)
     + (5 * j)) % 7
h = round(h)
if h == 1:
    h = Monday
elif h == 2:
    h = Tuesday
elif h == 3:
    h = Wednesday
elif h == 4:
    h = Thursday
elif h == 5:
    h = Friday
elif h == 6:
    h = Saturday
elif h == 0:
    h = Sunday


print(h)
