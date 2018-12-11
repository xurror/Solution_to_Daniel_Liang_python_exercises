''' Program to check whether a string is a substring of another string, without using inbuilt functions'''
  
def find(str1, str2):
    for i in range(0, len(str2)):
        if str2[i] == str1[0]:
            k=i
            for j in range(0, len(str1)):
                if str2[k] == str1[j]:
                    if j == len(str1)-1:
                        return True
                    k +=1
                else:
                    break
   
    return False


def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    x = find(str1, str2)
    if (x):
        print("String ", str1, "is a substring of String ", str2)
    else:
        print("String ", str1, "is not a substring of String ", str2)

main()