''' Function to find the longest common prefix in two strings'''

def prefix(s1, s2):
    preStr =""
    if len(s1) <= len(s2):
        n = len(s1)
    else:
        n = len(s2)
        
    for i in range(0, n):
        if s1[i] == s2[i]:
            preStr = preStr + s1[i]
        else:
            break

    return preStr


def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    x = prefix(str1, str2)
    print("Longest prefix of String1: ", str1, "and String2: ", str2,"is :", x)

main()