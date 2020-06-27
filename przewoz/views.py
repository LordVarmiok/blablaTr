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
        message = 'przejazdy'
        transits = Transit.objects.filter(driver=request.user)
        form = TransitForm()
        return render(request, 'list_and_add.html', {'objects': transits, 'form': form, 'message': message})

    def post(self, request):
        form = TransitForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.driver = request.user
            obj.save() # dodany automatycznie driver jako zalogowany uzytkownik
            return redirect("/przewoz/my_transits/")
        context = {'objects': Transit.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)


class MyTransitsView(View):
    def get(self, request):
        message = 'przejazdy'
        transits = Transit.objects.filter(driver=request.user)
        return render(request, 'my_transits.html', {'objects': transits, 'message': message})


class VehicleView(View):
    def get(self, request):
        message = 'pojazdy'
        form = VehicleForm()
        vehicles = Vehicle.objects.filter(driver=request.user)
        return render(request, 'list_and_add.html', {'objects': vehicles, 'form': form, 'message': message})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.driver = request.user
            obj.save()
            return redirect("/przewoz/my_vehicles/")
        context = {'objects': Vehicle.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)


class MyVehiclesView(View):
    def get(self, request):
        message = 'pojazdy'
        vehicles = Vehicle.objects.filter(driver=request.user)
        return render(request, 'my_vehicles.html', {'objects': vehicles, 'message': message})


class CargoView(View):
    def get(self, request):
        message = 'cargo'
        form = CargoForm()
        cargo = Cargo.objects.filter(owner=request.user)
        return render(request, 'list_and_add.html', {'objects': cargo, 'form': form, 'message': message})

    def post(self, request):
        form = CargoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            return redirect("/przewoz/my_cargo/")
        context = {'objects': Cargo.objects.all(), 'form': form}
        return render(request, 'list_and_add.html', context)


class MyCargoView(View):
    def get(self, request):
        message = 'cargo'
        cargo = Cargo.objects.filter(owner=request.user)
        return render(request, 'my_cargo.html', {'objects': cargo, 'message': message})
