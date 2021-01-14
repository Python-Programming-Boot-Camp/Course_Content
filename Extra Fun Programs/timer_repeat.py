import playsound
import time
minutes = int(input("How many minutes do you want to set your timer for: "))
number = int(input("How many times do you want the timer to repeat: "))
t = minutes * 60
for i in range (number):
        while t:
            mins = t // 60
            sec = t % 60
            timer = "{:02d}:{:02d}".format(mins,sec)
            print(timer, end = "\r")
            time.sleep(1)
            t-=1
        t = minutes * 60
        print("Timer")
        playsound.playsound(alarm.mp3)

