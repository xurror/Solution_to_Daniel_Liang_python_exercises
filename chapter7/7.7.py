#Program to solve linear equations
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
    a,b,c,d,e,f = eval(input("Enter Value for a,b,c,d,e,f: "))

    equation=LinearEquation(a,b,c,d,e,f)
  
    if equation.isSolvable():
        print("The Equation has no solution")
    else:
        print("The value for x:",equation.getX())
        print("The value for y:",equation.getY())
      

main()