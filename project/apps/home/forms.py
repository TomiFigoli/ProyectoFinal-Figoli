from django import forms
from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

class VendedorForm(forms.ModelForm):
    class Meta:
        model = models.Vendedor
        fields = "__all__"