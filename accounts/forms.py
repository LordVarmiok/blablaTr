from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email","username", "password1", "password2"]
