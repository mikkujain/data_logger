# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from devices.models import *
from django.utils.timezone import datetime #important if using timezones

from datetime import date


class Dashboard(ListView):
	model = (Devices, Mobile, Sms, Ports, Data)
	template_name = "dashboard.html"

	def get_queryset(self):
		today = date.today()
		queryset = Alert.objects.filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day)
		return queryset

	def get_context_data(self, **kwargs):
		today = datetime.today()
		# Call the base implementation first to get a context
		context = super(Dashboard, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['mobile'] = Mobile.objects.all()
		context["sms"] = Sms.objects.filter(datetime__year=today.year, datetime__month=today.month, datetime__day=today.day)
		dt = Data.objects.all()
		context["todayalert"] = [i.TodaysAlert() for i in dt]
		print(context)
		return context

		