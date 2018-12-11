'''Program to find the largest element in a 2D list'''


def locateLargest(a):
    l = [0,0]
    maxValue = a[0][0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if float(maxValue) < float(a[i][j]):
                maxValue = a[i][j]
                l[0] = i
                l[1] = j
    return l

def main():
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

    largest = locateLargest(matrix2D)
    
    print("The location of largest element is at (", largest[0], ",",largest[1],")")
    
main()