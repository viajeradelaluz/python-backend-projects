from django.urls import path

import apps.staff.views as v

app_name = "staff"

employee = [
    path("", v.EmployeeListView.as_view(), name="employee_list"),
    path("create/", v.EmployeeCreateView.as_view(), name="employee_create"),
    path("<int:pk>/", v.EmployeeDetailView.as_view(), name="employee_detail"),
    path("<int:pk>/update/", v.EmployeeUpdateView.as_view(), name="employee_update"),
    path("<int:pk>/delete/", v.EmployeeDeleteView.as_view(), name="employee_delete"),
]

department = [
    path(
        "department/",
        v.DepartmentListView.as_view(),
        name="department_list",
    ),
    path(
        "department/create/",
        v.DepartmentCreateView.as_view(),
        name="department_create",
    ),
    path(
        "department/<int:pk>/",
        v.DepartmentDetailView.as_view(),
        name="department_detail",
    ),
    path(
        "department/<int:pk>/update/",
        v.DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "department/<int:pk>/delete/",
        v.DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
]

urlpatterns = [*employee, *department]
