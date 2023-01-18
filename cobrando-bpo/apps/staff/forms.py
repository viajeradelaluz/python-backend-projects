from django.forms import ModelForm

from .models import Departamento, Empleado


class EmployeeForm(ModelForm):
    """Form definition for Empleado."""

    class Meta:
        model = Empleado
        fields = ["nit", "nombre", "apellido1", "apellido2", "codigo_departamento"]


class DepartmentForm(ModelForm):
    """Form definition for Departamento."""

    class Meta:
        model = Departamento
        fields = ["nombre", "presupuesto"]
