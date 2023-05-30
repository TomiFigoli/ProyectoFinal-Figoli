from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def index(request):
    return render(request, "home/index.html")

def agregar_cliente(request):
    if request.method=="POST":
       form = forms.ClienteForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request,"home/index.html")
    else:
        form=forms.ClienteForm
        contexto={"form":form}
    return render(request, "home/agregar_cliente.html", contexto)



def agregar_producto(request):
    if request.method=="POST":
       form = forms.ProductoForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request,"home/index.html")
    else:
        form=forms.ProductoForm
        contexto={"form":form}
    return render(request, "home/agregar_producto.html", contexto)
    

def agregar_vendedor(request):
    if request.method=="POST":
       form = forms.VendedorForm(request.POST)
       if form.is_valid():
           form.save()
           return render(request,"home/index.html")
    else:
        form=forms.VendedorForm
        contexto={"form":form}
    return render(request, "home/agregar_vendedor.html", contexto)

