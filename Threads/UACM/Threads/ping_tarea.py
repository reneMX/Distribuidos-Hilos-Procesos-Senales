#!/usr/bin/python3
import os
import threading
from random import randint
local = threading.local()
contador = 0

#host  = "192.168.31.126"
host2 = "192.168.31.
#respuesta = os.system("ping " + host) WINDOWS

#respuesta = os.system("ping -c 3 " + host)

#if respuesta == 0:
#   print( host, 'esta arriba')
#else:
#   print(host, 'esta abajo')


def run(local, barrier):
	#valores de 1 hasta 126.
	#local.my_value = randint(0, 10**2)
	global contador
	local.my_value = contador
	contador += 1
	t = threading.current_thread()
	print(f'Thread {t.name} has value {local.my_value}')
	barrier.wait()
	print(f'Thread {t.name} still value {local.my_value}')


count = 129
barrier = threading.Barrier(count)

threads = [
    threading.Thread(
	target=run, name=f'T{name}', args=(local, barrier)
    ) for name in range(count)
]

for t in threads:
	t.start()
