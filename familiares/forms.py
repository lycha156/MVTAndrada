from dataclasses import fields
from django import forms
from django import forms
from .models import Familiar

class FamiliarForm(forms.ModelForm):

    class Meta:
        model = Familiar
        fields = [
            'nombre',
            'apellido',
            'dni',
            'fechaNacimiento',
            'telefono',
            'direccion',
            'email'
        ]

    apellido = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
    nombre = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autofocus': 'autofocus'}))
    dni = forms.IntegerField(required=False, widget=forms.TextInput( attrs={'class': 'form-control', 'type': 'number', 'data-mask': '99999999', 'placeholder': 'DNI'}))
    fechaNacimiento = forms.DateField(required=False, widget=forms.DateInput(format = ('%Y-%m-%d'),attrs={ 'class': 'form-control', 'type': 'date', 'title': 'Fecha de Nacimiento'} ))
    telefono = forms.CharField(required=False, widget=forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Telefono'}))
    direccion = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicilio'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput( attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}))