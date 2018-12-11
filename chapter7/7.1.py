class rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    
    #Method to compute area
    def getArea(self):
        return (self.width * self.height)
        #print(area)
        
    #Method to computr perimeter
    def getPerimeter(self):
        return ((self.width + self.height) * 2)
               
        
Rectangle = rectangle(1, 2)
#print(Rectangle.getArea())
