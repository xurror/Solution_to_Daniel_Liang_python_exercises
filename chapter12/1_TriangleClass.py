'''Program to create rectangle class by inheriting Geometric object class'''

from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):  
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1
    def getSide2(self):  
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2
        
    def getSide3(self):  
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3
        
    
    def getArea(self):
        p = self.getPerimeter()
        area = (p*(p-self.__side1)*(p-self.__side2)*(p-self.__side3))**0.5
        return area
    
    def getPerimeter(self):
        return  (self.__side1 + self.__side2 + self.__side3)
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)
    
    
def main():
    s1,s2,s3 = eval(input("Enter the three sides of a Triangle: "))
    color = input("Enter the color of Triangle: ")
    isFilled = eval(input("Is Triangle filled(0/1): "))
    R = Rectangle(s1,s2,s3)
    R.setColor(color)
    R.setFilled(isFilled)
    
    print("Area is: ", R.getArea()," Perimeter is: ", R.getPerimeter(), " Color is:", R.getColor(), " Filled: ", str(R.isFilled()))
    
    
main()    