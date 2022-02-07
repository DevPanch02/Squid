from django import forms
from django.forms import fields, ModelForm, widgets
from core.products.models import Producto

class ProductoForms(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets={
            'categoriaName':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'autocomplete':'on',
                }
            ),

            'nombre':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre',
                    'autocomplete':'off',
                }
            ),
            'apellido':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Apellido',
                    'autocomplete':'off',
                }
            ),

            'direccion':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese direccion',
                    'autocomplete':'off',
                }
            ),
            'email':widgets.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese email',
                    'input_type':'email',
                    'autocomplete':'off',
                }
            ),

            'password':widgets.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese password',
                    'input_type':'password',
                    'autocomplete':'off',
                }
            ),
            
        }