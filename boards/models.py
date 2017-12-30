# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Competing_Organizations(models.Model):
    name= models.CharField(max_length=50, unique = True)
    representative = models.ForeignKey(User,related_name='competing_org_representative')
    points = models.DecimalField(max_digits = 5, decimal_places = 1)

class Awarding_Organizations(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    representative = models.ForeignKey(User,related_name='awarding_org_representative')

class Points(models.Model):
    points = models.DecimalField(max_digits=5, decimal_places=1)
    points_winner = models.ForeignKey(Competing_Organizations, related_name = 'points_winner')
    points_giver = models.ForeignKey(Awarding_Organizations, related_name = 'points_giver')
