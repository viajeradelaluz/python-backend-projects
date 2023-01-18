from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("", include("apps.home.urls", namespace="home")),
    path("admin/", admin.site.urls),
    path("staff/", include("apps.staff.urls", namespace="staff")),
]

urlpatterns += staticfiles_urlpatterns()
