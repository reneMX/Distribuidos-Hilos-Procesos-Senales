port = 21
banner = "FTPServer"
print ("[+] Validando "+banner+" en puerto "+str(port))
type(banner)
type(port)
portList=[21,22,80,110]
type(portList)
portOpen = True
type(portOpen)
version = 2.03
type(version)
version = "2.03-4"
type(version)
print (banner.upper())
print (banner.lower())
print (banner.replace('FTP','WWW'))
print (banner.find('FTP'))
print (banner[0]+banner[1])
print (banner[-1]+banner[-2])
portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
print (portList)
portList.sort()
print (portList)
pos = portList.index(80)
print ("[+] Hay "+str(pos)+" puerto(s) abiertos antes del puerto 80.")
portList.remove(443)
print (portList)
cnt = len(portList)
print ("[+] Existen"+str(cnt)+" Puertos abiertos.")
print (portList[2])
lista=[1,20,3,40]
lista.append(5)
lista  
lista.sort()   
lista  
lista.remove(40)  
lista  
lista.index(3)
lista  
lista.insert(0,0) 
lista  
lista.reverse()
lista
lista.pop(2)
lista  
lista2 = [0,0,0]
lista.extend(lista2)
lista
lista.count(0)
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
print (services.items())
print (services.keys())
print (services.values())
print ('ftp' in services)
print (services['ftp'])
print ("[+] Servicio FTP en puerto "+str(services['ftp']))
print (type(services))
