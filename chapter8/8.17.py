''' The Point Class '''

class Point():
    def __init__(self,x = 0,y= 0):
        self.x=x
        self.y=y
    
    def __str__(self):
        s = "("+ self.x + "," + self.y +")"
        return s 

    def getX(self):
        return self.x
    def getY(self):
        return self.y
         
    def distance(self, P1):
        x2 = P1.getX()
        y2 = P1.getY()
        D = ((self.x-x2)**2 + (self.y-y2)**2)**.5
        return D 
  
    def isNearby(self, P1):
        if(self.distance(P1) <= 5):
            print("The points are near each other")
        else:
            print("The points are not near each other")
        
  
def main():
    x1,y1,x2,y2 = eval(input("Enter two points x1,y1,x2,y2: "))
    P1 = Point(x1,y1)
    P2 = Point(x2,y2)
  
    print("The distance between the two points is", P1.distance(P2))
    P1.isNearby(P2)

main()
