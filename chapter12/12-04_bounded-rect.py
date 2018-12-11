# Liang 12.4
from Rectangle2D import *

def getRectangle(points):
    xVals = [float(points[x]) for x in range(len(points)) if x % 2 == 0]
    yVals = [float(points[y]) for y in range(len(points)) if y % 2 != 0]
    xMax, yMax, xMin, yMin = max(xVals), max(yVals), min(xVals), min(yVals)
    x = (xMax + xMin) / 2
    y = (yMax + yMin) / 2

    return Rectangle2D(x, y, abs(xMax - xMin), abs(yMax - yMin))

def main():
    points = input('Enter the points: ')
    rect = getRectangle(points.split())
    print ('The bounding rectangle is centered at (%0.2f, %0.2f) with width %0.2f and height %0.2f' \
            % (rect.getX(), rect.getY(), rect.getWidth(), rect.getHeight()))

if __name__ == '__main__':
    main()
