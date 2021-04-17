#!/usr/bin/python3
import threading
from time import sleep
from random import random


counter = 0
randsleep = lambda: sleep(0.1 * random())


def incr(n):
    global counter
    for count in range(n):
        incr_lock.acquire()
        try:
            current = counter
            randsleep()
            counter = current + 1
            randsleep()
        finally: 
            incr_lock.release()


n = 5
incr_lock = threading.Lock()
t1 = threading.Thread(target=incr, args=(n, ))
t2 = threading.Thread(target=incr, args=(n, ))

t1.start()
t2.start()

t1.join()
t2.join()
print(f'Counter: {counter}')

