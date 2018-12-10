import time
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60

print(chr(currentSecond))