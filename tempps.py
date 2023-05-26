import time
def Timer(seconds):
    for i in range(seconds):
        time.sleep(1)
        seconds -= 1
        print(seconds)
    if seconds == 0:
        return(seconds)
print(Timer(20))