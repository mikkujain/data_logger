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
from graphos.renderers.gchart import LineChart

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
		# Add in a QuerySet of all the books
		context['mobile'] = Mobile.objects.all()
		context["sms"] = Sms.objects.filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day)
		context["max_level"] = context["data_list"].aggregate(Max('value'))["value__max"]
		context["min_level"] = context["data_list"].aggregate(Min('value'))["value__min"]
		context["avg_level"] = context["data_list"].aggregate(Avg('value'))["value__avg"]
		context["last_sms"] = context["sms"].latest("datetime").datetime
		data =  [
				['Year', 'Sales', 'Expenses'],
				[2004, 1000, 400],
				[2005, 1170, 460],
				[2006, 660, 1120],
				[2007, 1030, 540]
			]
		chart = LineChart(SimpleDataSource(data=data), width="100%")
		context["chart"] = chart
		print(context)
		return context