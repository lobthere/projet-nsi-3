from threading import Thread, Timer
from time import sleep

def _timer(_time):
    class ThreadCustom(Thread):

        def __init__(self):
            Thread.__init__(self)
            self.value = None

        def test(self, imi):
            self.time = imi

        def run(self):
            sleep(self.time)
            self.value = 'hello world!'


    thread = ThreadCustom()
    thread.test(_time)
    thread.start()
    thread.join()
    data = thread.value
    return data