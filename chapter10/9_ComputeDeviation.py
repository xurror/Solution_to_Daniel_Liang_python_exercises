'''Program to compute deviation'''

def mean(x):
    sum1 = 0.0
    mean = 0.0
    for i in range(len(x)):
        sum1 += x[i]
    mean = (sum1/len(x))
    return mean

def deviation(x):
    sum1 = 0.0
    mean1 = mean(x)
    for i in range(len(x)):
        sum1 += (x[i] - mean1)**2  
    stddev = (sum1/ (len(x) -1))**0.5
    return stddev


def main():
    list1 = eval(input("Enter numbers: "))
    print("The mean is :", mean(list1))
    print("The standard deviation is" , deviation(list1))
    
main()
