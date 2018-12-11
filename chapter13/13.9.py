# L 13.9
import pickle

def decrypt(ifile, ofile):
    infile = open(ifile, 'rb')
    outfile = open(ofile, 'w')
    s = pickle.load(infile)
    try:
        while s != '':
            outfile.write(chr(ord(s)-5))
            s = pickle.load(infile)
    except EOFError:
        infile.close()
        outfile.close()
    return 'Done'

def main():
    ifile, ofile = input('Enter name of input and output file: ').split(',')
    print (decrypt(ifile, ofile))

if __name__ == '__main__':
    main()

