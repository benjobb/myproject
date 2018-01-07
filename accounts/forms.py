from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from boards.models import *

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    awarding_organization = forms.ModelChoiceField(
        queryset = Awarding_Organizations.objects.all(),
        error_messages={'required': 'Please enter your organization'},
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
