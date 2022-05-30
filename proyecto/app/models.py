from django.db import models

class Personas(models.Model):

    nombre = models.CharField(max_length= 40)
    edad = models.IntegerField()
    mail = models.EmailField()
    comentario = models.CharField(max_length=50)

   

class Productos(models.Model):

    nombre = models.CharField(max_length= 40)
    numero_serie = models.IntegerField()
    nui = models.IntegerField()


class Ventas(models.Model):

    nombre_comprador = models.CharField(max_length= 40)
    mail_comprador = models.EmailField()
    numero_pedido = models.IntegerField()
    