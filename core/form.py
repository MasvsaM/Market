from django import forms
from django.forms import ModelForm
from .models import Cliente, Producto
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

            'fec_nac':forms.DateInput(
                attrs={
                    'placeholder':'Debe ingresar Apellido',
                    'class':'form-control',
                    "type":"date",
                    }
            ),

            'telefono':forms.NumberInput(
                attrs={
                    'placeholder':'Debe ingresar Telefono',
                    'class':'form-control'
                    }
            ),
            'correo':forms.EmailField(
                attrs={
                    'placeholder':'Debe ingresar correo electronico',
                    'class':'form-control'
                }
            ),
            
            'contraseña': forms.CharField(
                widget= 'forms.PasswordInput',
                attrs={
                    'placeholder':'Ingrese contraseña',
                    'class':'form-control'
                }
            ),

            'confirmacion': forms.CharField(
                widget= 'forms.PasswordInput',
                attrs={
                    'placeholder':'Ingrese nuevamente contraseña',
                    'class':'form-control'
                }
            ),

            'rut':forms.IntegerField(
                attrs={
                    'placeholder':'Debe ingresar rut',
                    'class':'form-control'
                }
            ),

            'region':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar Region',
                    'class':'form-control'
                }
            ),
            

            'direccion':forms.TextInput(
                attrs={
                    'placeholder':'Debe ingresar Direccion',
                    'class':'form-control'
                }
            ),

            'cod_postal':forms.CharField(
                attrs={
                    'placeholder':'Debe ingresar Codigo Postal',
                    'class':'form-control'
                }
            ),

            'comentario':forms.CharField(
                attrs={
                    'placeholder':'Debe ingresar Codigo Postal',
                    'class':'form-control'
                }
            )
        }
    
class ProductoFrom(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widget={
            'modelo':forms.CharField(
                attrs= {
                        'placeholder':'Debe ingresar modelo',
                        'class': 'form-control'
                }
            ),
            'tipo':forms.Select(
                attrs= {
                        'placeholder':'Debe escoger una marca',
                        'class': 'form-control'
                }
            ),
            'marca':forms.Select(
                attrs= {
                        'placeholder':'Debe escoger una marca',
                        'class': 'form-control'
                }
            ),
            'file':forms.ImageField(
                attrs= {
                        'placeholder':'Debe ingresar uns imagen',
                        'class': 'form-control'
                }
            ),
            'precio':forms.NumberInput(
                attrs= {
                        'placeholder':'Debe ingresar precio',
                        'class': 'form-control'
                }
            ),

            'stock':forms.NumberInput(
                attrs= {
                        'placeholder':'Debe ingresar precio',
                        'class': 'form-control'
                }
            ),

            'comentario':forms.CharField(
                attrs= {
                        'placeholder':'Descripcion del celular',
                        'class': 'form-control'
                }
            )
            
        }