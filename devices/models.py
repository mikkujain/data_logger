# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
# from django.utils.timezone import datetime 
from datetime import date
from django.utils.timezone import datetime


class Devices(models.Model):
	device_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=255)

	def __str__(self):
		return '{} id {}'.format(self.device_id, self.name)

class Ports(models.Model):
	port_name = models.CharField(max_length=5, unique=True)
	device = models.ForeignKey(Devices, on_delete=models.CASCADE)
	datetime = models.DateTimeField(default=datetime.now, blank=True)
	alert_level = models.FloatField()


	unique_together = (("device", "port_name"),)

	def __str__(self):
		return '{} Alert level {}'.format(self.port_name, self.alert_level)

class Data(models.Model):
	port = models.ForeignKey(Ports, on_delete=models.CASCADE)
	value = models.FloatField()
	datetime = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return 'port {} value {} datetime {}'.format(self.port, self.value, self.datetime.strftime("%Y-%m-%d %I:%M %p"))

	def TodaysAlert(self):
		today = datetime.today()
		if self.datetime__year==today.year and datetime__month==today.month and datetime__day==today.day and self.value > self.port.alert_level:
			return self

class Mobile(models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '9999999999'. 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
	

	def __str__(self):
		return '{}'.format(self.phone_number)

class Sms(models.Model):
	data = models.ForeignKey(Data, on_delete=models.CASCADE)
	to = models.ForeignKey(Mobile, on_delete=models.CASCADE)
	message = models.TextField()
	datetime = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return '{}'.format(self.to)


	
