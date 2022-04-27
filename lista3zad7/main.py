import time
import timer

def timer_gen():
    start = time.time()
    while True:
        yield time.time() - start


if __name__ == '__main__':

    time_class = timer.Timer()

    for now in timer_gen(): # albo in time_class
        print(now)
