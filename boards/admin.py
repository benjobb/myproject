# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Competing_Organizations)
admin.site.register(Awarding_Organizations)
admin.site.register(Points)
