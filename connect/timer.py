import time

class Timer(object):
    def __init__(self,start):
        self.start =start

    def print(self):
        now = time.time()
        print('耗时:',now-self.start)