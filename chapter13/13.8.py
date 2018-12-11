# L 13.8
import pickle

def encrypt(ifile, ofile):
    infile = open(ifile, 'r')
    outfile = open(ofile, 'wb')
    for line in infile:
        for word in line:
            for char in word:
                pickle.dump(chr(ord(char)+5), outfile)
    infile.close()
    outfile.close()
    return 'Done'

def main():
    ifile, ofile = input('Enter name of input and output file: ').split(',')
    print (encrypt(ifile, ofile))

if __name__ == '__main__':
    main()

