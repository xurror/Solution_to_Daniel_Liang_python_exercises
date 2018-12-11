''' Function to convert a binary number to hexadecimal '''

def binaryToHex(binaryValue):
    bin1 = binaryValue
    base = 1
    dec = 0
    HexValue = ""
    # First convert binary to decimal
    while (bin1 > 0):
        rem = bin1 % 10
        dec = dec + rem * base;
        base = base * 2;
        bin1 = bin1 // 10;
    
    # Then convert decimal to hexadecimal
    while dec != 0 :
        temp = dec % 16
        if( temp < 10):
            temp = temp + 48
        else:
            temp = temp + 55;
        HexValue = chr(temp) + HexValue 
        dec = dec // 16;
    
    
    return HexValue

def main():
    bin1 = eval(input("Enter the binary number: "))
    print("The hexadecimal equivalent of ",bin1,"is: ", binaryToHex(bin1))
    
main()