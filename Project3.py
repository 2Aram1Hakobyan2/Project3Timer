def convertet():
    hours = Seconds//3600
    minutes = (Seconds//60)%60
    ss = Seconds%60
    print("Time Left - ",hours,":",minutes , ":", ss)

import random
import time
phrase = ["Set a timer", "Timer variables should be inserted", "Countdown should be set"]
rndphrase = random.choice(phrase)
print(rndphrase)
h = int(input('Hours : '))
m = int(input('Minutes : '))
s = int(input('Seconds : '))
Seconds = h*3600+m*60+s
while Seconds!=0:
    minutes = Seconds//60
    ss = Seconds%60
    time.sleep(1)
    convertet()
    Seconds-=1
    if Seconds==0:
        print("Time Left -  0 : 0 : 0")
        print("Time is Up!!! ")
        break
        #Pull Request is open
