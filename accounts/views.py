from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm, UpdateProfile


# Create your views here.
# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = 'registration/signup.html'
#
#     def form_valid(self, form):
#         obj = super().form_valid(form)
#         # superlos = Group.objects.get(pk=1)
#         # self.object.groups.add(superlos)
#         return obj


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, 'registration/signup.html', {'form': form})


class UpdateProfileView(View):
    def get(self, request):
        form = UpdateProfile()
        context = {'form': form}
        return render(request, 'registration/update_profile.html', context)

    def post(self, request):
        form = UpdateProfile(request.POST, instance=request.user)
        form.actual_user = request.user
        context = {'form': form, 'message':'Zmieniono dane konta'}
        if form.is_valid():
            form.save()
            return render(request, 'registration/update_profile.html', context)


# def update_profile(request):
#     args = {}
#
#     if request.method == 'POST':
#         form = UpdateProfile(request.POST, instance=request.user)
#         form.actual_user = request.user
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('updateSuccess'))
#         else:
#             form = UpdateProfile()
#             args['form'] = form
#
#         return render(request, 'registration/update_profile.html', args)


def successEditProfile(request):
    message = "Zmieniono dane konta"
    return render(request, 'registration/success_update_profile.html', {'message': message})