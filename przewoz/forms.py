from django import forms
from django.core.exceptions import ValidationError
from przewoz.models import Transit, Vehicle, Cargo, Reservation


class TransitForm(forms.ModelForm):
    class Meta:
        model = Transit
        exclude = ["driver"]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ["driver"]


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        exclude = ["owner"]


class TransitSearchForm(forms.Form):
    # model = Transit
    query = forms.CharField(required=False)
    # fields = "__all__"


class MakeReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['driver']