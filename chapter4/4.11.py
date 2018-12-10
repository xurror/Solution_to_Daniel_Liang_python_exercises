actualYear = eval(input("Enter the actual year: "))
month, year = eval(input("Enter the numerical equivalent of a month and it's year: "))

January = 'January'
February = 'February'
March = 'March'
April = 'April'
May = 'May'
June = 'June'
July = 'July'
August = 'August'
September = 'September'
October = 'October'
November = 'November'
December = 'December'

#Check for leap year
leapYear = year % 4

if month == 1:
    month = January
    monthdays = 31
elif month == 3:
    monthdays = 31
    month = March
elif month == 4:
    monthdays = 30
    month = April
elif month == 5:
    monthdays = 31
    month = May
elif month == 6:
    monthdays = 30
    month = June
elif month == 7:
    monthdays = 31
    month = July
elif month == 8:
    monthdays = 31
    month = August
elif month == 9:
    monthdays = 31
    month = September
elif month == 10:
    monthdays = 31
    month = October
elif month == 11:
    monthdays = 30
    month = November
elif month == 12:
    monthdays = 31
    month = December

if year == actualYear:
    if leapYear != 0:
        if month == 2:
            monthdays = 28
            month = February
        print(month, year, "has", monthdays, "days")

    else:
        if month == 2:
            month = February
            monthdays = 29
        print(month, year, "has", monthdays, "days")

elif year > actualYear:
    if leapYear != 0:
        if month == 2:
            monthdays = 28
            month = February
        print(month, year, "will have", monthdays, "days")

    else:
        if month == 2:
            month = February
            monthdays = 29
        print(month, year, "will have", monthdays, "days")

else:
    
    if leapYear != 0:
        if month == 2:
            monthdays = 28
            month = February
        print(month, year, "had", monthdays, "days")

    else:
        if month == 2:
            month = February
            monthdays = 29
        print(month, year, "had", monthdays, "days")
    
