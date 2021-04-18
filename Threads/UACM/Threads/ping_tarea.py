#!/usr/bin/python3
import os
import threading
import time
local = threading.local()
contador = 0

def run(local, barrier):
	#valores de 1 hasta 126
	global contador
	global host
	host = "192.168.31." + str(contador)
	contador += 1
	respuesta = os.system("ping -c 3 " + host)

	local.my_value = contador

	if respuesta == 0:
		print(host, 'Esta Arriba')
	else:
		print(host, 'Esta Abajo')

	t = threading.current_thread()
	print(f'Hilo {t.name} con valor previo {local.my_value}')

	barrier.wait()
	print(f'Hilo {t.name} con valor final {local.my_value}')



count = 126
barrier = threading.Barrier(count)

threads = [
    threading.Thread(
	target=run, name=f'T{name}', args=(local, barrier)
    ) for name in range(count)
]

for t in threads:
	t.start()
