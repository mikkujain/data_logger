# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from devices.models import *
from django.utils.timezone import datetime #important if using timezones
from django.db.models import Max, Min, Avg
from datetime import date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from graphos.sources.simple import SimpleDataSource
from graphos.renderers import gchart

class Dashboard(LoginRequiredMixin, ListView):
	model = (Devices, Mobile, Sms, Ports, Data)
	template_name = "dashboard.html"
	login_url = '/'

	def get_queryset(self):
		queryset = Data.objects.all()
		return queryset

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(Dashboard, self).get_context_data(**kwargs)
		startd = self.request.GET.get('start-date')
		endd = self.request.GET.get('end-date')
		if self.request.GET.get('date'):
			try:
				today = datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d').date()
				context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
			except Exception as e:
				context['errors'] = ["Invalid Date Format Selected"]
		elif startd and endd:
			try:
				startd = datetime.strptime(startd, '%Y-%m-%d').date()
				endd = datetime.strptime(endd, '%Y-%m-%d').date()
				context["data_list"] = context["data_list"].filter(datetime__date__range=[startd, endd])
			except Exception as e:
				context['errors'] = ["Invalid Date Format Selected"]
		else:
			today = datetime.today()
			context["data_list"] = context["data_list"].filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
			dv = Devices.objects.all()
			context["device1"] = context["data_list"].filter(port__device=dv[0])
			context["device2"] = context["data_list"].filter(port__device=dv[1])
		context['mobile'] = Mobile.objects.all()
		context["device1_max"] = context["device1"].aggregate(Max('value'))["value__max"]
		context["device2_max"] = context["device2"].aggregate(Max('value'))["value__max"]
		context["device1_min"] = context["device1"].aggregate(Min('value'))["value__min"]
		context["device2_min"] = context["device2"].aggregate(Min('value'))["value__min"]	
		context["device1_avg"] = context["device1"].aggregate(Avg('value'))["value__avg"]
		context["device2_avg"] = context["device2"].aggregate(Avg('value'))["value__avg"]
		context["today_alert_times"] = len([i for i in context['data_list'] if i.value > i.port.alert_level])
		#context["last_sms"] = context["sms"].latest("datetime").datetime
		data = []
		if context['data_list']:
			data = [['DateTime', 'Water']]
			for i in context['data_list']:
				data.append([i.datetime.strftime("%d/%m/%y %H:%I %p"), i.value])
			chart = gchart.LineChart(SimpleDataSource(data=data), options={'title': 'Water Level'}, height=400, width=600)
			context["chart"] = chart
		return context
