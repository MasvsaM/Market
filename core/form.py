from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteFrom(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widget={
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar un Nombre',
                    'class':'form-control'
                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar Apellido',
                    'class':'form-control'
                }
            ),

            'fecha_nacimiento':forms.DateInput(
                format='%d/%m/%Y',
                attrs=dict(
                    type="date",
            )
            


        }