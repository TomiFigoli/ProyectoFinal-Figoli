from django import forms
from . import models

class ClientesForm(forms.ModelForm):
    class Meta:
        model = models.Clientes
        fields = "__all__"

class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Productos
        fields = "__all__"

class VendedoresForm(forms.ModelForm):
    class Meta:
        model = models.Productos
        fields = "__all__"