import sqlite3
from datetime import datetime
import time
import urllib.request
import urllib.parse
import json

conn = sqlite3.connect("db.sqlite3")

def sendSMS(apikey, numbers, sender, message):
	# data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
	# 	'message' : message, 'sender': "TXTLCL", 'test': True})
	# data = data.encode('utf-8')
	# request = urllib.request.Request("https://api.textlocal.in/send/?")
	# f = urllib.request.urlopen(request, data)
	# fr = f.read()
	# return(fr)
	return '{"test_mode":true,"balance":9,"batch_id":99,"cost":1,"num_messages":1,"message":{"num_parts":1,"sender":"TXTLCL","content":"This is your message"},"receipt_url":"","custom":"","messages":[{"id":1,"recipient":919742856795}],"status":"success"}'

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
		print("create data")
		sql = """insert into devices_data ('port_id', 'value', 'datetime') values (?, ?, ?);"""
		try:
			print("start try")
			c.execute(sql,(key, str(val), time.strftime('%Y-%m-%d %H:%M:%S')))
			print("executed")
			conn.commit()
			print("commited")
			createSms(val, c.lastrowid)
			print("end try")
		except Exception as e:
			print("exception",e)
		print("commited")
	c.close()
	print("closed")


def createSms(val, data_id):
	print("val and data id", val, data_id)
	c = conn.cursor()
	nums = c.execute("select * from devices_mobile;")
	print("fetched nums query")
	apikey = "6Bwh/Aw5zOQ-oz0GbW0obUCMWu5bhP3WOxQ08iMFUD"
	message = 'This is your message'
	nums = [int(i[1]) for i in nums.fetchall()]
	print("nums list", nums)
	resp =  sendSMS(apikey, nums, 'TXTLCL', message)
	resp = json.loads(resp)
	print("resp is", resp)
	if resp["status"] == "success":
		for i in range(resp["num_messages"]):
			sql_num_id = """select id from devices_mobile where phone_number = ?"""
			c.execute(sql_num_id, (resp["messages"][i]["recipient"],))
			for i in c:
				print("fetch num id", i, "and ", i.fetchall())
			sql = """insert into devices_sms ('data_id', 'to_id', 'message') values (?, ?, ?);"""
			try:
				c.execute(sql,(data_id, str(val), message))
				conn.commit()
				print("sms created adn send")
			except Exception as e:
				print(e)
			print("commited")
	c.close()