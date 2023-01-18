from django.urls import path

import apps.home.views as v

app_name = "home"

urlpatterns = [path("", v.HomeMainView.as_view(), name="main")]
