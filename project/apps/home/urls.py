from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('agregar-cliente', views.agregar_cliente, name="agregar-cliente"),
    path('agregar-prodcuto', views.agregar_producto, name="agregar-producto"),
    path('agregar-vendedor', views.agregar_vendedor, name="agregar-vendedor"),

]
