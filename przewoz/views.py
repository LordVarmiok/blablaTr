from django.shortcuts import render, redirect
from django.views import View

from przewoz.models import Transit, Vehicle, Cargo
from przewoz.forms import TransitForm, VehicleForm, CargoForm

APP_VERSION = '0.1'


# Create your views here.
def index(request):
    return render(request, 'base.html', {'app_version': APP_VERSION})


class TransitView(View):
    def get(self, request):
        transits = Transit.objects.filter(driver=request.user)
        form = TransitForm()
        return render(request, 'list_and_add.html', {'objects': transits, 'form': form})

    def post(self, request):
        form = TransitForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.driver = request.user
            obj.save() # dodany automatycznie driver jako zalogowany uzytkownik
            return redirect("/przewoz/transits/")
        context = {'objects': Transit.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)


class VehicleView(View):
    def get(self, request):
        form = VehicleForm()
        vehicles = Vehicle.objects.all()
        return render(request, 'list_and_add.html', {'objects': vehicles, 'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/przewoz/vehicles/")
        context = {'objects': Vehicle.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)


class CargoView(View):
    def get(self, request):
        form = CargoForm()
        cargo = Cargo.objects.all()
        return render(request, 'list_and_add.html', {'objects': cargo, 'form': form})

    def post(self, request):
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/przewoz/cargo/")
        context = {'objects': Cargo.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)



class MyVehicles(View):
    def get(self, request, id):
        vehicles = Vehicle.objects.filter(driver__vehicle=id)
        return render(request, 'list_and_add.html', {'objects': vehicles})