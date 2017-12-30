# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import *


# Create your views here.


from django.http import HttpResponse

def home(request):
    competing_orgs = Competing_Organizations.objects.all()
    return render(request,'home.html', {'competing_orgs':competing_orgs})

def competing_orgs(request, pk):
    org = Competing_Organizations.objects.get(pk=pk)
    return render(request, 'competing_orgs.html', {'org':org})

class NewPoints(CreateView):
    model = Points
    form_class = Point_Form
    success_url = reverse_lazy('home')
    template_name = 'newpoints.html'
