# Liang 7.8
import time

class StopWatch:

    def __init__(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return round(self.__endTime - self.__startTime, 3)

def main():
    watch = StopWatch()
    nSum = 0
    LIMIT = int(1e6)

    watch.start()
    for i in range(LIMIT):
        nSum += 1
        
    watch.stop()
    print ('Execution time: %.3f' % watch.getElapsedTime())

if __name__ == '__main__':
    main()
