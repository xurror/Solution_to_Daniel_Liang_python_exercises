# Liang 6.34
import math

def area(n, side):
    return (n * (side * side)) / (4 * math.tan(math.pi / n))

def main():
    n = int(input('Enter the number of sides (n > 2): '))
    side = float(input('Enter the side length (length > 0): '))
    print ('The area of the polygon is %f' % area(n, side))

if __name__ == '__main__':
    main()
