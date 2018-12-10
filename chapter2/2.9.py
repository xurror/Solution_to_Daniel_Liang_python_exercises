ta = eval(input("Enter the temperature in Fahrenheit between -58 and 41 : "))
v = eval(input("Enter the wind speed in miles per hour : "))

if v >= 2:
    
    twc = 35.74 + (0.6215 * ta) - (35.75 * (v ** 0.16)) + (0.4275 * ta * (v ** 0.16))
    print("The wind chill is", twc)

else :

    print("Sorry but the wind speed is too small to be evaluated")
