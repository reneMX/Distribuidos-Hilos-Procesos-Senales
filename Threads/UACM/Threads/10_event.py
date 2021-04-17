#!/usr/bin/python3
import threading
from time import sleep

def fire():
    print('Firing event...')
    event.set()


def listen():
    print('Waiting for event')
    event.wait()
    print('Event has been fired')


event = threading.Event()
t1 = threading.Thread(target=fire)
t2 = threading.Thread(target=listen)
t2.start()
sleep(3)
t1.start()
