# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from devices.models import *
from django.utils.timezone import datetime #important if using timezones
from django.db.models import Max, Min, Avg
from datetime import date

from graphos.sources.simple import SimpleDataSource
from graphos.renderers import gchart

class Dashboard(ListView):
	model = (Devices, Mobile, Sms, Ports, Data)
	template_name = "dashboard.html"

	def get_queryset(self):
		today = date.today()
		queryset = Data.objects.filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day).order_by("datetime")
		return queryset

	def get_context_data(self, **kwargs):
		today = datetime.today()
		# Call the base implementation first to get a context
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['mobile'] = Mobile.objects.all()
		context["sms"] = Sms.objects.filter(data__datetime__year=today.year, data__datetime__month=today.month, data__datetime__day=today.day)
		context["max_level"] = context["data_list"].aggregate(Max('value'))["value__max"]
		context["min_level"] = context["data_list"].aggregate(Min('value'))["value__min"]
		context["avg_level"] = context["data_list"].aggregate(Avg('value'))["value__avg"]
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