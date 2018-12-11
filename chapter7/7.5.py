#Program to make a n sided regular Polygon using classes
import math

class RegularPolygon():
    def __init__(self=1,n=3,side=1,x=0,y=0):
        self.n=n
        self.side=side
        self.x=x
        self.y=y
        
    def getPerimeter(self):
        return self.n*self.side
   
    def getArea(self):
        return ((self.n)*(self.side)**2)/(4*(math.tan(math.pi/self.n)))
   
def main():
    polygon1=RegularPolygon()
    polygon2=RegularPolygon(6,4)
    polygon3=RegularPolygon(10,4,5.6,7.8)
  
  
    print("Polygon1 perimeter is:",polygon1.getPerimeter(),"\n polygon1 Area is:",polygon1.getArea())
    print("Polygon2 perimeter is:",polygon2.getPerimeter(),"\n polygon2 Area is:",polygon2.getArea())
    print("polygon3 perimeter is:",polygon3.getPerimeter(),"\n polygon3 Area is:",polygon3.getArea())
    
main()