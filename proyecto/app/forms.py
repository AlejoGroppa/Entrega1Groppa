from django import forms

class PersonasFormulario(forms.Form):

    nombre = forms.CharField(max_length= 40)
    edad = forms.IntegerField()
    mail = forms.EmailField()
    comentario = forms.CharField(max_length=50)

   

class ProductosFormulario(forms.Form):

    nombre = forms.CharField(max_length= 40)
    numero_serie = forms.IntegerField()
    nui = forms.IntegerField()


class VentasFormulario(forms.Form):

    nombre_comprador = forms.CharField(max_length= 40)
    mail_comprador = forms.EmailField()
    numero_pedido = forms.IntegerField()
    