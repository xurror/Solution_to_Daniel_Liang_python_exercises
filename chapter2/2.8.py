M = eval(input("Enter the amount of water in kilogramme : "))
initial_temperature = eval(input("Enter the initial temperature : "))
final_temperature = eval(input("Enter the final temperature : "))

Q = M * (final_temperature - initial_temperature) * 4182

print("The energy needed is", Q)
