#Program to find the first days of all months by the given year and January 1 of that year

year = eval(input("Enter the year: "))
first = eval(input("Enter the first day of the year: "))
days = 0

for m in range(1,12 + 1):
    if m == 1:
        print("January 1", year, "is ", end = "")
        days = 31
    elif m == 2:
        print("February 1",year, "is ", end = "")
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            days = 29
        else:
            days = 28
    elif m == 3:
        print("March 1,", year, "is ", end = "")
        days = 31
    elif m == 4:
        print("April 1,", year, "is ", end = "")
        days = 30
    elif m == 5:
        print("May 1,", year, "is ", end = "")
        days = 31
    elif m == 6:
        print("June 1,", year, "is ", end = "")
        days = 30
    elif m == 7:
        print("July 1,", year, "is ", end = "")
        days = 31
    elif m == 8:
        print("August 1,", year, "is ", end = "")
        days = 31
    elif m == 9:
        print("September 1,", year, "is ", end = "")
        days = 30
    elif m == 10:
        print("October 1,", year, "is ", end = "")
        days = 31
    elif m == 11:
        print("November 1,", year, "is ", end = "")
        days = 30
    elif (m == 12):
        print("December 1,", year, "is ", end = "")
        days = 31


    if first == 0:
        print("Sunday") 
    elif first == 1:
        print("Monday") 
    elif first == 2:
        print("Tuesday") 
    elif first == 3:
        print("Wednesday") 
    elif first == 4:
        print("Thursday") 
    elif first == 5:
        print("Friday") 
    elif first == 6:
        print("Saturday") 

    first = (first + days) % 7
