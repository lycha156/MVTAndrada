from django.db import models

class Familiar(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    dni = models.IntegerField("DNI", null=True, blank=True)
    fechaNacimiento = models.DateField("Fecha de Nacimiento", auto_now=False, auto_now_add=False, null=True, blank=True)
    telefono = models.CharField("Telefono", max_length=50, null=True, blank=True)
    direccion = models.CharField("Direccion", max_length=50, null=True, blank=True)
    email = models.EmailField("Email", max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    



