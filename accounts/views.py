from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        obj = super().form_valid(form)
        # superlos = Group.objects.get(pk=1)
        # self.object.groups.add(superlos)
        return obj
