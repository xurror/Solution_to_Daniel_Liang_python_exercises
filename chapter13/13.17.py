# L 13.17
import urllib.request

def computeSalary(infile):
    staffs = ['assistant', 'associate', 'full']
    salary = [[0,0], [0,0], [0,0]]
    currStaff = infile.readline().decode().split()
    while currStaff != []:
        s = staffs.index(currStaff[2])
        salary[s][0] += float(currStaff[3])
        salary[s][1] += 1
        currStaff = infile.readline().decode().split()
    return salary

def main():
    # url = input('Etner the URL for a file: ')
    url = 'http://cs.armstrong.edu/liang/data/Salary.txt'
    infile = urllib.request.urlopen(url)

    tSals = computeSalary(infile)
    st1, st2, st3 = tSals[0][0], tSals[1][0], tSals[2][0]
    n1, n2, n3 = tSals[0][1], tSals[1][1], tSals[2][1]
    # computeAvgSalary(s)

    print ('Total Salary\n%s %15.2f \n%s %15.2f \n%s %20.2f \n%s %13.2f' % \
          ('Assistant salary:', st1, 'Associate salary:', st2, 'Full salary:', st3, \
           'All Faculty salary:', st1+st2+st3))

    print ('\nAverage Salary\n%s %15.2f \n%s %15.2f \n%s %20.2f \n%s %13.2f' % \
          ('Assistant salary:', st1 / n1, 'Associate salary:', st2 / n2, 'Full salary:', st3 / n3, \
           'All Faculty salary:', (st1+st2+st3)/(n1+n2+n3)))
                                                                   

if __name__ == '__main__':
    main()
