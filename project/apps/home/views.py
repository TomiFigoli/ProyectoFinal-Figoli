from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def agregar_cliente(request):
    form = forms.ClientesForm()
    contexto={"form":form}
    return render(request, "home/agregar_cliente.html", contexto)

def agregar_producto(request):
    form = forms.ProductosForm()
    contexto={"form":form}
    return render(request, "home/agregar_producto.html", contexto)

def agregar_vendedor(request):
    form = forms.VendedoresForm()
    contexto={"form":form}
    return render(request, "home/agregar_vendedor.html", contexto)

