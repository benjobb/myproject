# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *
from .forms import *
from django.db import transaction


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory


# Create your views here.

from django.http import HttpResponse

@login_required
def home(request):
    competing_orgs = Competing_Organizations.objects.all()
    for org in competing_orgs:
        org.points = 0
        points_awarded = Points.objects.filter(points_winner=org)
        for point in points_awarded:
            org.points +=point.points
            org.save()

    return render(request,'home.html', {'competing_orgs':competing_orgs})

def competing_orgs(request, pk):
    org = Competing_Organizations.objects.get(pk=pk)
    return render(request, 'competing_orgs.html', {'org':org})

class NewPoints(CreateView):
    model = Points
    form_class = Point_Form
    success_url = reverse_lazy('home')
    template_name = 'newpoints.html'

    def get_context_data(self, **kwargs):
        data = super(NewPoints, self).get_context_data(**kwargs)
        if self.request.POST:
            data['points_storage'] = PointFormSet(self.request.POST)
        else:
            data['points_storage'] = PointFormSet()
        return data


    def form_valid(self, form):
        username = self.request.user
        form.instance.points_giver = Awarding_Organizations.objects.get(representative= username)


        return super(NewPoints, self).form_valid(form)
