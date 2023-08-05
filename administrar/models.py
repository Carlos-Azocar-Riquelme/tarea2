from django.db import models


# Create your models here.
class Tarea(models.Model):

    #Modificación de este campo, pongo el default para que sepa que poner en este nuevo       parámetro
    titulo = models.CharField(max_length=64,
                              blank=False,
                              null=False,
                              default="---")

    #Estado 0. Indica tarea pendiente
    #Estado 1, Indica tarea completada
    estado = models.BooleanField(default=0)
