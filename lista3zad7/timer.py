import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def __next__(self):
        return time.time() - self.start

    def __iter__(self):
        return self

