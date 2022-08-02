import time

class Timer:
    def start(self):self.start_count = time.time()
    def stop(self):self.end_count = time.time()
    def get(self):return "%.4f" % (self.end_count - self.start_count)
timer = Timer()
