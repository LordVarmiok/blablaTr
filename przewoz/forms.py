from django import forms
from django.core.exceptions import ValidationError
from przewoz.models import Transit, Vehicle


class TransitForm(forms.ModelForm):
    class Meta:
        model = Transit
        fields = "__all__"


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"


class CargoForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"