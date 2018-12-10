ta = eval(input("Enter the temperature in Fahrenheit between -58 and 41 : "))
v = eval(input("Enter the wind speed in miles per hour : "))

if v >= 2 and (ta > -58 and ta < 41):
    
    twc = 35.74 + (0.6215 * ta) - (35.75 * (v ** 0.16)) + (0.4275 * ta * (v ** 0.16))
    print("The wind chill is", twc)

elif v < 2 and (ta < -58 or ta > 41):

    print("Sorry but the wind speed is too small to be evaluated and your temperature is out of range")

elif v < 2:
    print("Sorry but the wind speed is too small")

elif (ta < -58 or ta > 41):
    print("Sorry but the temperature is out of range")
