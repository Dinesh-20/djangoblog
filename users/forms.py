# Created a custom form page that inherits base UserCreationForm and add custom fields according to usage

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adding additional field on Base User from. By default, required is TRUE

    class Meta:   # Provides a namespace that stores the configuration of the data that is to be displayed or received
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Adding additional field on Base User from. By default, required is TRUE

    class Meta:  # Provides a namespace that stores the configuration of the data that is to be displayed or received
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



