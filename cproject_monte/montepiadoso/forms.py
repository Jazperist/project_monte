from django import forms
from .models import Cliente

class ClienteCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "apellido", "telefono", "email", "fecha_inicio", "cantidad_pedida", "plazo")
