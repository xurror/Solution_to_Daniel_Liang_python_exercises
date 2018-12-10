integer = eval(input("Enter an integer: "))

mod5 = integer % 5
mod6 = integer % 6

##if mod5 == 0 and mod6 == 0:
print("Is", str(integer), "divisible by 5 and 6?", (mod5 == 0) and (mod6 == 0))

##if mod5 == 0 or mod6 == 0:
print("Is", str(integer), "divisible by 5 or 6?", (mod5 == 0) or (mod6 == 0))

##if (mod5 == 0 or mod6 == 0) != (mod5 and mod6):
print("Is", str(integer), "divisible by 5 or 6?", ((mod5 == 0) or (mod6 == 0)) != ((mod5 == 0) and (mod6 == 0)))
