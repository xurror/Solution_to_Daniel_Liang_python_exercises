# Liang 8.19

class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def containsPoint(self, x, y):
        return abs(x - self.x) <= self.width/2 and abs(y - self.y) <= self.height/2

    def contains(self, other):
        return ((self.x <= other.x ) and (self.x <= self.width)) \
               and ((other.x + other.width) <= (self.x + self.width)) \
               and ((other.y + other.height) <= (self.y + self.height))

    def overlaps(self, other):
        return not(self.x <= other.x  or self.x <= self.width \
               or ((other.x + other.width) <= (self.x + self.width)) \
               or ((other.y + other.height) <= (self.y + self.height)))

    def __contains__(self, other):
        return ((self.x >= other.x) and (self.y >= other.y)) \
               and ((other.x + other.width) >= (self.x + self.width)) \
               and ((other.y + other.height) >= (self.y + self.height))

    def __cmp__(self, other):
        if self.getArea() > other.getArea():
            return 1
        elif self.getArea() < other.getArea():
            return -1
        else:
            return 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0


def main():
    r1 = input('Enter x, y, width, height: ')
    r2 = input('Enter x, y, width, height: ')
    r1 = [float(v) for v in r1.split(',')]
    r2 = [float(v) for v in r2.split(',')]

    r1 = Rectangle2D(r1[0], r1[1], r1[2], r1[3])
    r2 = Rectangle2D(r2[0], r2[1], r2[2], r2[3])

    print ('Area for %s is %0.1f' % ('r1', r1.getArea()))
    print ('Perimeter for %s is %0.1f' % ('r1', r1.getPerimeter()))
    print ('Area for %s is %0.1f' % ('r2', r2.getArea()))
    print ('Perimeter for %s is %0.1f' % ('r2', r2.getPerimeter()))
    print ('%s contains the center of %s? %r' % ('r1', 'r2', r1.containsPoint(r2.x, r2.y)))
    print ('%s contains %s? %r' % ('r1', 'r2', r1.contains(r2)))
    print ('%s overlaps %s %r' % ('r1', 'r2', r1.overlaps(r2)))
    

if __name__ == '__main__':
    main()
