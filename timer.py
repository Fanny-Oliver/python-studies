#Python program to create a countdown timer

import time
t = int(input("Enter time in seconds here: "))

def countdown (time_sec):
    while time_sec:
        mins, secs = divmod(t, 60)
        timer = '(:02d) : (:02d)'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        time_sec -= 1
        print ("Time up!")

countdown (t)