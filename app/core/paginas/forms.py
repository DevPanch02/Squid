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
            'paginas':widgets.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Paginas',
                    'autocomplete':'on',
                }
            ),
        }
