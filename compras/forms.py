from django.forms import ModelForm
from .models import Compra, ItemCompra

class FormCompra(ModelForm):
    class Meta:
        model = Compra
        exclude = ['protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
        