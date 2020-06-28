from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

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


class UpdateTransitView(View):
    model = Transit
    fields =['description']
    template_name = "update_object.html"
    success_url = reverse_lazy('myTransits')


class DeleteTransitView(DeleteView):
    model = Transit
    template_name = "delete_transit.html"
    success_url = reverse_lazy("myTransits")


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


class UpdateVehicleView(View):
    model = Vehicle
    fields =['description']
    template_name = "update_object.html"
    success_url = reverse_lazy('myVehicles')


class DeleteVehicleView(DeleteView):
    model = Vehicle
    template_name = "delete_vehicle.html"
    success_url = reverse_lazy("myVehicles")


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


class UpdateCargoView(View):
    model = Cargo
    fields =['description']
    template_name = "update_object.html"
    success_url = reverse_lazy('myCargo')


class DeleteCargoView(DeleteView):
    model = Cargo
    template_name = "delete_cargo.html"
    success_url = reverse_lazy("myCargo")