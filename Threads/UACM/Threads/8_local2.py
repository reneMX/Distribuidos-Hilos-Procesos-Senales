#!/usr/bin/python3
import threading
from random import randint
from time import sleep


def corre():
    global local
    local = randint(0, 10**2)
    t = threading.current_thread()
    print(f'Thread {t.name} has value {local}')
    sleep(.1)
    print(f'Thread {t.name} still has value {local}')

count = 3


threads = [
    threading.Thread(
        target=corre, name=f'T{name}',
    ) for name in range(count)
]

for t in threads:
    t.start()


