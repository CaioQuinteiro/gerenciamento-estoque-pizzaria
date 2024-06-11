from django.forms import ModelForm
from .models import Compra

class FormServico(ModelForm):
    class Meta:
        model = Compra
        exclude = ['protocolo', 'identificador']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
