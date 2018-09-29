# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


admin.site.register(Devices)
admin.site.register(Ports)
admin.site.register(Data)
admin.site.register(Mobile)
# admin.site.register(Alert)
admin.site.register(Sms)