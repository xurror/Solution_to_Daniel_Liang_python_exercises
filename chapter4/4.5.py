today = eval(input("Enter today's day: "))
elapsedDays = eval(input("Enter the number of days elapsed since today: "))

Monday = 'Monday'
Tuesday = 'Tuesday'
Wednesday = 'Wednesday'
Thursday = 'Thursday'
Friday = 'Friday'
Saturday = 'Saturday'
Sunday = 'Sunday'


futureDay = today + elapsedDays

if today == 1:
    today = Monday
elif today == 2:
    today = Tuesday
elif today == 3:
    today = Wednesday
elif today == 4:
    today = Thursday
elif today == 5:
    today = Friday
elif today == 6:
    today = Saturday
elif today == 0:
    today = Sunday

futureday = futureDay % 7

if futureday == 1:
    futureDay = Monday
elif futureday == 2:
    futureDay = Tuesday
elif futureday == 3:
    futureDay = WWednesday
elif futureday == 4:
    futureDay = Thursday
elif futureday == 5:
    futureDay = Friday
elif futureday == 6:
    futureDay = Saturday
elif futureday == 0:
    futureDay = Sunday
    
print("Today is", today, "and the future day is", futureDay)
