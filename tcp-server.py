import socket
from tcpFunctions import *

s = socket.socket()
s.bind(("localhost",5000))
s.listen(5)
dic = {}

while True:
	c, addr = s.accept()
	data = c.recv(1024)
	data = data.decode('utf-8').split(";")
	for i in data:
		try:
			dic[i.split(":")[0]] = i.split(":")[1]
		except Exception as e:
			print(e, "for i", i)
	ports = getDevice(dic["#STH"])
	values = {}
	if ports:
		for p in ports:
			values[p[0]] = dic[p[1]]
		print("values", values)
		createData(values)
		print("created data")
	c.close()

