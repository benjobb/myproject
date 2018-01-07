from django import forms
from .models import *
from django.forms import ModelForm, inlineformset_factory
from django.forms.models import modelformset_factory

class Point_Form(forms.ModelForm):
    points = forms.DecimalField(label='Points to be awarded')

    class Meta:
        model = Points
        fields = ['points', 'points_winner']

PointFormSet = modelformset_factory(Points, Point_Form)
