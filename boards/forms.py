from django import forms
from .models import *

class Point_Form(forms.ModelForm):
    points = forms.DecimalField(label='Points to be awarded')

    class Meta:
        model = Points
        fields = ['points', 'points_winner']
