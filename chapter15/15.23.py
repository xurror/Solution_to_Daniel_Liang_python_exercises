# (String permutation) Write a recursive function to print all the permutations of a
# string. For example, for the string abc, the printout is:
# abc
# acb
# bac
# bca
# cab
# cba
# (Hint: Define the following two functions. The second function is a helper function.
# def displayPermuation(s):
# def displayPermuationHelper(s1, s2):
# The    first    function    simply    invokes    displayPermuation(" ", s).The    second    function    uses    a
# loop    to    move    a    character    from s2 to    s1 and recursively    invokes    it    with a new s1 and s2.
# The base case is that s2 is empty and prints s1 to the    console.)    Write    a     test    program    that
# prompts    the    user    to    enter    a    string and displays    all    its    permutations.

def displayPermutation(s):
    displayPermutationHelper(" ", s)

def displayPermutationHelper(s1, s2):
    if len(s2) == 0:
        print(s1)
    # else:
    for i in range(len(s2)):
        # print(s1)
        displayPermutationHelper(s1 + s2[i], s2[0:i] + s2[i+1:len(s2)])

displayPermutation("abc")

#
# def permutations(s,l,r):
#
#     if l==r:
#         str1=tostring(s)
#         print(str1)
#     else:
#         for i in range(l,r+1):
#
#             s[l],s[i]=s[i],s[l]
#
#             permutations(s,l+1,r)
#
#             s[l], s[i] = s[i], s[l]
#
#
# def tostring(s):
#     str1 = ''.join(s)
#     return str1
#
# b="abc"
# a=list(b)
# permutations(a,0,len(b)-1)