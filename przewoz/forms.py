from django import forms
from django.core.exceptions import ValidationError
from przewoz.models import Transit, Vehicle, Cargo


class TransitForm(forms.ModelForm):
    class Meta:
        model = Transit
        exclude = ["driver"]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"
