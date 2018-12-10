n = eval(input("Enter an integer: "))
# number of spaces
k = 2*n - 2
left = 1
right = 1
 
# outer loop to handle number of rows
for i in range(0, n):

    left = 1
    # inner loop to handle number spaces
    # values changing acc. to requirement
    #for j in range(0, k):
       # print(end=" ")
        
        #right = 2
    #num = 1
     
    # decrementing k after each loop
        #k = k - 1
     
    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i+1):

        
        # printing stars
        print(left, end=" ")
        left = n - 1
        #right = right + 1
        #right = num + 1
    # ending line after each row
    print("\r")
        
    # incrementing number at each column
    #num = num + 1
     
    # ending line after each row
print("\r")
