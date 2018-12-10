import math

print("degree \t   sin \t\t cos")
degree = 0

for degree in range(0, 365, 10):

    sin = math.sin(degree)
    cos = math.cos(degree)

    print(str(degree)
          + str(format(sin, "15.4f"))
          + str(format(cos, "15.4f")))
