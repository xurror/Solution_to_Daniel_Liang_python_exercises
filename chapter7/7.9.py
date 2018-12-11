#Program to find the intersecting point of 2 lines
import math

class LinearEquation():
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.d
    def getE(self):
        return self.e
    def getF(self):
        return self.f
    
    def isSolvable(self):
        if (self.a*self.d)-(self.b*self.c)==0:
            return True
    
    def getX(self):
        return ((self.e*self.d)-(self.b*self.f))/((self.a*self.d)-(self.b*self.c))
    
    def getY(self):
        return ((self.a*self.f)-(self.e*self.c))/((self.a*self.d)-(self.b*self.c))
    

def main():
    x1,y1,x2,y2=eval(input("Enter the endpoints of the first line segment"))
    x3,y3,x4,y4=eval(input("Enter the endpoints of the second line segment"))
    a=y1-y2
    b=(-x1)+x2
    c=y3-y4
    d=(-x3)+x4
    e=-y1*(x1-x2)+(y1-y2)*x1
    f=-y3*(x3-x4)+(y3-y4)*x3
    
    temp=LinearEquation( a, b, c, d, e, f)
  
    if temp.isSolvable():
        print("The two lines are parallel")
    else:
        print("The intersecting point is: (",temp.getX(),",",temp.getY(),")")  
  
main()
