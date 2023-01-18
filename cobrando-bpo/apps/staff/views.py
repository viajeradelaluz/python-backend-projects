from django.urls import reverse_lazy
from django.views import generic

from .forms import DepartmentForm, EmployeeForm
from .models import Departamento, Empleado


class EmployeeCreateView(generic.CreateView):
    """Render employee creation page."""

    model = Empleado
    form_class = EmployeeForm
    template_name = "staff/employee/create.html"
    extra_context = {"departments": Departamento.objects.all()}
    success_url = reverse_lazy("staff:employee_list")


class EmployeeListView(generic.ListView):
    """Render employee list page."""

    model = Empleado
    template_name = "staff/employee/list.html"
    context_object_name = "employees"


class EmployeeDetailView(generic.DetailView):
    """Render employee detail page."""

    model = Empleado
    template_name = "staff/employee/detail.html"
    context_object_name = "employee"


class EmployeeUpdateView(generic.UpdateView):
    """Render employee update page."""

    model = Empleado
    form_class = EmployeeForm
    template_name = "staff/employee/update.html"
    extra_context = {"departments": Departamento.objects.all()}
    context_object_name = "employee"
    success_url = reverse_lazy("staff:employee_list")


class EmployeeDeleteView(generic.DeleteView):
    """Render employee delete page."""

    model = Empleado
    template_name = "staff/employee/delete.html"
    context_object_name = "employee"
    success_url = reverse_lazy("staff:employee_list")


class DepartmentCreateView(generic.CreateView):
    """Render department creation page."""

    model = Departamento
    form_class = DepartmentForm
    template_name = "staff/department/create.html"
    success_url = reverse_lazy("staff:department_list")


class DepartmentListView(generic.ListView):
    """Render department list page."""

    model = Departamento
    template_name = "staff/department/list.html"
    context_object_name = "departments"


class DepartmentDetailView(generic.DetailView):
    """Render department detail page."""

    model = Departamento
    template_name = "staff/department/detail.html"
    context_object_name = "department"


class DepartmentUpdateView(generic.UpdateView):
    """Render department update page."""

    model = Departamento
    form_class = DepartmentForm
    template_name = "staff/department/update.html"
    context_object_name = "department"
    success_url = reverse_lazy("staff:department_list")


class DepartmentDeleteView(generic.DeleteView):
    """Render department delete page."""

    model = Departamento
    template_name = "staff/department/delete.html"
    context_object_name = "department"
    success_url = reverse_lazy("staff:department_list")
