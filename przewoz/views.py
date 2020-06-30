from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, UpdateView

from przewoz.models import Transit, Vehicle, Cargo, Reservation
from przewoz.forms import TransitForm, VehicleForm, CargoForm, TransitSearchForm, MakeReservationForm
import random
APP_VERSION = '0.1'


# Create your views here.
def index(request):
    '''
    :param request:
    :return: Widok pokazuje glowna strone z randomowym pojazdem, randomowym przejazdem i randomowym cargo
    '''
    vehicles = Vehicle.objects.filter(driver=request.user)
    transits = Transit.objects.filter(driver=request.user)
    cargo = Cargo.objects.filter(owner=request.user)

    vehicles_pk_num = []
    transits_pk_num = []
    cargo_pk_num = []
    # petle zapelniaja tablice z pk kazdych modeli
    for element in vehicles:
        vehicles_pk_num.append(element.pk)

    for element in transits:
        transits_pk_num.append(element.pk)

    for element in cargo:
        cargo_pk_num.append(element.pk)

    vehicle = vehicles.filter(pk=random.choice(vehicles_pk_num))
    transit = transits.filter(pk=random.choice(transits_pk_num))
    cargo = cargo.filter(pk=random.choice(cargo_pk_num))

    context = {'app_version': APP_VERSION,'vehicle': vehicle, 'transit': transit, 'cargo': cargo}
    return render(request, 'home_random.html', context)


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


class SearchTransitView(View):
    def get(self, request):
        transits_all = Transit.objects.all()
        search_form1 = TransitSearchForm(request.GET)
        search_form1.is_valid()
        destination = search_form1.cleaned_data.get('do', "")
        q1 = Q(destination__icontains=destination)
        arrival = search_form1.cleaned_data.get('z', "")
        q2 = Q(place_of_departure__icontains=arrival)
        transits = Transit.objects.filter(q1 & q2)
        # return transits, search_form
        return render(request, 'search_form.html',
                      {'objects_all': transits_all, 'objects': transits, 'search_form1': search_form1})


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


class UpdateVehicleView(UpdateView):
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


class MakeReservationView(View):
    def get(self, request, pk):
        form = MakeReservationForm()
        transit = Transit.objects.filter(pk=pk)
        cargo = Cargo.objects.filter(owner=request.user)
        # vehicle = Vehicle.objects.filter(transit__vehicle_id__exact=transit.vehicle)
        return render(request, 'make_reservation.html', {'form': form, 'transit': transit, 'cargo': cargo})

    def post(self, request, pk):
        form = MakeReservationForm(request.POST)
        transit = Transit.objects.get(pk=pk)
        cargo = Cargo.objects.filter(owner=request.user)
        #vehicle = Vehicle.objects.filter(transit__vehicle_id__exact=transit.vehicle)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.driver = transit.driver
            obj.vehicle = transit.vehicle
            obj.save()
            return redirect('/przewoz/my_reservations/')
        return render(request, 'make_reservation.html', {'form': form, 'transit': transit, 'cargo': cargo})


class MyReservationsView(View):
    def get(self, request):
        message = 'rezerwacje'
        reservations = Reservation.objects.filter(cargo__owner=request.user)
        return render(request, 'my_reservation.html', {'objects': reservations, 'message': message})


class TransitReservationsView(View):
    def get(self, request, pk):
        message = 'rezerwacje na przejazdach'
        transit = Transit.objects.filter(pk=pk)
        reservations = Reservation.objects.filter(transit__driver=request.user)
        return render(request, 'transit_reservation.html', {'objects': reservations, 'message': message, 'transit':transit})