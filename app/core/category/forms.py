from django.db.models import fields
from django.forms import ModelForm, widgets

from core.category.models import Categoria

class CategoryForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

       
        widgets={
            'nombre':widgets.TextInput(
                attrs={
                    'id':'name_product',
                    'class':'form-control',
                    'placeholder':'Ingrese categoria',
                    'autocomplete':'off',
                }
            ),
            

        }
