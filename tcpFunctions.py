import sqlite3
from datetime import datetime
import time
from urllib2 import Request
from urllib2 import urlopen
from urllib import urlencode
import json

conn = sqlite3.connect("db.sqlite3")

def sendSMS(apikey, numbers, sender, message):
	data =  urlencode({'apikey': apikey, 'numbers': numbers,
		'message' : message, 'sender': "TXTLCL", 'test': True})
	data = data.encode('utf-8')
	request = Request("https://api.textlocal.in/send/?")
	f = urlopen(request, data)
	fr = f.read()
	return(fr)
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
			c.execute(sql,(key, str(val), time.strftime('%Y-%m-%d %H:%M:%S')))
			conn.commit()
			createSms(val, c.lastrowid)
		except Exception as e:
			print("exception",e)
		print("commited")
	c.close()
	print("closed")


def createSms(val, data_id):
	print("val and data id", val, data_id)
	c = conn.cursor()
	num_fetch = c.execute("select * from devices_mobile;")
	num_fetch_all = num_fetch.fetchall()
	apikey = "6Bwh/Aw5zOQ-oz0GbW0obUCMWu5bhP3WOxQ08iMFUD"
	message = 'This is your message'
	nums = [i[1] for i in num_fetch_all]
	nums_id = [i[0] for i in num_fetch_all]
	print("nums and nums_id", nums, nums_id)
	resp =  sendSMS(apikey, nums, 'TXTLCL', message)
	resp = json.loads(resp)
	print("resp is", resp)
	if resp["status"] == "success":
		for i in nums_id:
			sql = """insert into devices_sms ('data_id', 'to_id', 'message') values (?, ?, ?);"""
			try:
				c.execute(sql,(data_id, i, message))
				conn.commit()
				print("sms created adn send")
			except Exception as e:
				print(e)
			print("commited")
	c.close()