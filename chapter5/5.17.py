num = 33
codeList = []

for num in range(33, 127):
    codeList.append(chr(num))

while codeList != []:            
    for i in range(0, 10):
    
        if codeList != []:
            print(min(codeList), end=" ")
            codeList.pop(0)
    print()
