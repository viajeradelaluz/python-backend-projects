from django.views.generic import TemplateView


class HomeMainView(TemplateView):
    """Home main view."""

    template_name = "home/main.html"
