# import SocketServer

# class MyTCPHandler(SocketServer.BaseRequestHandler):

#     def handle(self):
#         self.data = self.request.recv(1024).strip()
#         print "{} wrote:".format(self.client_address[0])
#         print self.data
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
#     server.serve_forever()

import socket
import sqlite3



def getDevice(did):
	conn = sqlite3.connect("db.sqlite3")
	cur = conn.cursor
	c = conn.cursor()
	print("device dkjghjid", did)
	c = c.execute("select * from devices_devices where device_id = {}".format(str(did)))
	print(c)
	conn.close()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

s= socket.socket()

host = socket.gethostname()
port = 8000

s.bind((host,port))

s.listen(5)

#dic = {}

# while True:
# 	c, addr = s.accept()
# 	print("Got connection", addr)
# 	data = c.recv(1024)
# 	data = data.decode('utf-8').split(";")
# 	for i in data:
# 		try:
# 			dic[i.split(":")[0]] = i.split(":")[1]
# 		except Exception as e:
# 			print(e)
#c.close()

dic = {'P06': '00000000', 'K01': '10000000000', 'T': '01', 'P03': '64924223', 'A01': '0.000', 'A02': '00000', 'TM': '140620120347', 'A07': '00000', 'C': '04', 'A10': '27.00', 'L': '264', 'A04': '25.20', 'A06': '00000', 'A03': '0.975', 'A11': '31.81', 'O01': '0000', 'P05': '00000000', 'P02': '00000000', 'P01': '12345681', '#STH': '000002,000', 'A09': '35.48', 'D': '5', 'A05': '00000', 'P04': '03725855', 'A08': '00000'}
device = getDevice(dic["#STH"])






