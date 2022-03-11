from django import forms
from django.forms import fields, ModelForm, widgets
from core.usersquid.models import Usersquid

class UsersquidForms(ModelForm):
    class Meta:
        model = Usersquid
        fields = ('categoria','nombre','apellido','direccion','email','username','password','estado')

        widgets={
            'categoria':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'autocomplete':'on',
                }
            ),

            'nombre':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus nombres',
                    'autocomplete':'off',
                }
            ),

            'apellido':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                    'autocomplete':'off',
                }
            ),

            'direccion':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su dirección',
                    'autocomplete':'off',
                }
            ),

            'email':widgets.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                    'input_type':'email',
                    'autocomplete':'off',
                }
            ),

            'username':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                    'input_type':'text',
                    'autocomplete':'off',
                }
            ),

            'password':widgets.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una contraseña',
                    'input_type':'password',
                    'autocomplete':'off',
                }
            ),

            'estado':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'estado',
                    'autocomplete':'on',
                }
            )
        } 

class UsersquidPublicForms(ModelForm):
    class Meta:
        model = Usersquid
        fields = ('categoria','nombre','apellido','direccion','email','username','password')

        widgets={
            'categoria':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'autocomplete':'on',
                }
            ),

            'nombre':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus nombres',
                    'autocomplete':'off',
                }
            ),

            'apellido':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                    'autocomplete':'off',
                }
            ),

            'direccion':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su dirección',
                    'autocomplete':'off',
                }
            ),

            'email':widgets.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                    'input_type':'email',
                    'autocomplete':'off',
                }
            ),

            'username':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                    'input_type':'text',
                    'autocomplete':'off',
                }
            ),

            'password':widgets.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una contraseña',
                    'input_type':'password',
                    'autocomplete':'off',
                }
            )
        } 


class UpdateUsersquidForms(ModelForm):
    class Meta:
        model = Usersquid
        fields = ('categoria','nombre','apellido','direccion','email','estado')

        widgets={
            'categoria':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'autocomplete':'on',
                }
            ),

            'nombre':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus nombres',
                    'autocomplete':'off',
                }
            ),

            'apellido':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos',
                    'autocomplete':'off',
                }
            ),

            'direccion':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su dirección',
                    'autocomplete':'off',
                }
            ),

            'email':widgets.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su correo electrónico',
                    'input_type':'email',
                    'autocomplete':'off',
                }
            ),

            'estado':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'estado',
                    'autocomplete':'on',
                }
            )
        } 

class UpdatePasswordUsersquidForms(ModelForm):
    class Meta:
        model = Usersquid
        fields = ('username','password',)

        widgets={
            'username':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                    'input_type':'text',
                    'autocomplete':'off',
                }
            ),
            'password':widgets.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la nueva contraseña',
                    'input_type':'password',
                    'autocomplete':'off',
                }
            )
        } 