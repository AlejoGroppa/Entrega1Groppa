from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from app.forms import PersonasFormulario, VentasFormulario, ProductosFormulario
from app.models import Personas, Productos, Ventas
# Create your views here.

def inicio(request):

      return render(request, "app/inicio.html")


def personaFormulario(request):

    if request.method == 'POST':

        miFormulario = PersonasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            persona = Personas (nombre = informacion['nombre'], edad = informacion['edad'], mail = informacion['mail'], comentario = informacion['comentario'])
            
            persona.save()
            
            return render(request, "app/inicio.html")
    else:
        miFormulario = PersonasFormulario()

        return render(request, "app/persona.html", {"miFormulario":miFormulario})


        
def productoFormulario(request):

    if request.method == 'POST':

        miFormulario = ProductosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto = Productos (nombre = informacion['nombre'], numero_serie = informacion['numero_serie'], nui = informacion['nui'])
            
            producto.save()
            
            return render(request, "app/inicio.html")
    else:
        miFormulario = ProductosFormulario()

        return render(request, "app/producto.html", {"miFormulario":miFormulario})

def ventaFormulario(request):

    if request.method == 'POST':

        miFormulario = VentasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            venta = Ventas (nombre_comprador = informacion['nombre_comprador'], mail_comprador = informacion['mail_comprador'], numero_pedido = informacion['numero_pedido'])
            
            venta.save()
            
            return render(request, "app/inicio.html")
    else:
        miFormulario = VentasFormulario()

        return render(request, "app/producto.html", {"miFormulario":miFormulario})




def buscarPersona(request):

      if  request.GET["nombre"]:

            nombre = request.GET['nombre'] 
            personas = Personas.objects.filter(nombre__icontains=nombre)

            return render(request, "app/inicio.html", {"personas":personas, "nombre":nombre})

      else: 

            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)


def buscarProducto(request):

      if  request.GET["numero_serie"]:

            numero_serie = request.GET['numero_serie'] 
            productos = Productos.objects.filter(numero_serie__icontains=numero_serie)

            return render(request, "app/inicio.html", {"productos":productos, "numero_serie":numero_serie})

      else: 

            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)



def buscarVenta(request):

      if  request.GET["numero_pedido"]:

            numero_pedido = request.GET['numero_pedido'] 
            ventas = Ventas.objects.filter(numero_pedido__icontains=numero_pedido)

            return render(request, "app/inicio.html", {"ventas":ventas, "numero_pedido":numero_pedido})

      else: 

            respuesta = "No enviaste datos"
            return HttpResponse(respuesta)