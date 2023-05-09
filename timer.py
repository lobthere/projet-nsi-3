from threading import Thread, Timer
from time import sleep

class ThreadCustom(Thread, tome: int):

    def __init__(self):
        self.time = tome
        Thread.__init__(self)
        self.value = None

    def run(self):
        sleep(tome)
        self.value = 'Hello World!'

thread = ThreadCustom()
thread.start()
thread.join()
data = thread.value
print(data)