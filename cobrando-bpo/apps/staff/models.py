from django.db import models
from django.urls import reverse


class Empleado(models.Model):
    """Model definition for Empleado."""

    codigo = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey("Departamento", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("staff:employee_detail", args=[self.pk])  # type: ignore


class Departamento(models.Model):
    """Model definition for Departamento."""

    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.FloatField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("staff:department_detail", args=[self.pk])  # type: ignore
