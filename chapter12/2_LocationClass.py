'''Program to create location class - to locate largest number'''

class Location():
    def __init__(self, row = 0, column = 0, maxValue = 0.0):
        self.row = row
        self.column = column
        self.maxValue = maxValue
       
    def getrow(self):  
        return self.row

    def setrow(self, row):
        self.row = row
        
    def getcolumn(self):  
        return self.column

    def setcolumn(self, column):
        self.column = column
        
    def getMaxValue(self):  
        return self.maxValue
    

    def locateLargest(self, a):
        self.maxValue = a[0][0]
        for i in range(len(a)):
            for j in range(len(a[i])):
                if float(self.maxValue) < float(a[i][j]):
                    self.maxValue = a[i][j]
                    self.row = i
                    self.column = j
            

    

def printMatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end =" ")
        print()
    
def Input2DMatrix():
    row, col = eval(input("Enter the number of rows and columns in the list: "))
    matrix2D = []
    for i in range(row):
        matrix2D.append([])
        print("Enter row ", i, " :", end = " ")
        input1 = input()
        eleCol = input1.split(" ")
        k = 0
        for j in range(col):
            matrix2D[i].append(eleCol[k])
            k +=1
            
    return matrix2D
    
def main():
    inputmatrix = Input2DMatrix() 
    printMatrix(inputmatrix)
    l = Location()
    l.locateLargest(inputmatrix)
    
    print("The Location of Largest element is", l.maxValue, "at (",l.getrow(),",",l.getcolumn(),")")
    
main()    