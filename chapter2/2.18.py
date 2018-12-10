GMT_offset = eval(input("Enter the time zone offset to GMT : "))

import time
currentTime = time.time()

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60
currentHour = (totalHours % 24) + GMT_offset


print("Current time is", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
