weight = eval(input("Enter the weight in pounds: "))
feet = eval(input("Enter height in feet: "))
inches = eval(input("Enter height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
height = inches

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH

BMI = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", format(BMI, ".2f"))

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")

