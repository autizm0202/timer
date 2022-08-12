from threading import Timer
import time 



def countdowntimer(seconds):
    while seconds >0:

     mins = int(seconds/60)
     sec= int(seconds%60)
     timer = f'{mins}:{sec}'
     print(timer)
     seconds -= 1

print("timesup")

seconds = input("enter the time in seconds please:")

countdowntimer (int(seconds))
