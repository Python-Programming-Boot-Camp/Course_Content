import playsound
import time
t = int(input("Input how many minutes to set a time for: ")) * 60
while t:
    mins = t // 60
    sec = t % 60
    timer = "{:02d}:{:02d}".format(mins,sec)
    print(timer, end = "\r")
    time.sleep(1)
    t-=1
    print("Timer")
playsound.playsound(alarm.mp3)