import sqlite3
conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor

def getPorts(did):
	c = conn.cursor()
	c = c.execute("select id,port_name from devices_ports where device_id = {}".format(did))
	l = []
	for i in c:
		l.append(i)
	print("l is",l)
	return l

def getDevice(did):
	c = conn.cursor()
	try:
		did = did.split(",")[0]
	except Exception as e:
		print(e)
	c = c.execute("select id,name from devices_devices where device_id = {}".format(did))
	for i in c:
		print("i is", i)
		return getPorts(i[0])

def createData(value):
	c = conn.cursor()
	for key, val in value.items():
		c = c.execute("insert into devices_data ('port_id', 'value', 'datetime') values ({}, {})".format(key, val, ''))
		c.commit()
	c.close()