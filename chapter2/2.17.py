weight_pounds = eval(input("Enter weight in pounds : "))
height_inches = eval(input("Enter height in inches : "))

weight_kilo = 0.45359237 * weight_pounds
height_meters = 0.0254 * height_inches

BMI = weight_kilo / (height_meters ** 2)

print('BMI =', BMI)
