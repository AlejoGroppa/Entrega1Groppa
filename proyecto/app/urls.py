from django.urls import path
from app import views


urlpatterns = [
   
    path('inicio', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('personaFormulario', views.personaFormulario, name="personaFormulario"),
    path('productoFormulario', views.productoFormulario, name="productoFormulario"), 
    path('ventaFormulario', views.ventaFormulario, name="ventaFormulario"), 
    path('buscarPersona/', views.buscarPersona, name="buscarPersona"), 
    path('buscarProducto/', views.buscarProducto, name="buscarProducto"), 
    path('buscarVenta/', views.buscarVenta, name="buscarVenta"), 

]