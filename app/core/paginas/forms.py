from django.forms import fields, ModelForm, widgets
from core.paginas.models import Paginas

class paginaForm(ModelForm):
    class Meta:
        model=Paginas
        fields='__all__'

        widgets={
            'usuario':widgets.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'autocomplete':'on',
                }
            ),
            'nombre':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la página web a bloquear',
                    'autocomplete':'on',
                }
            ),
        }
