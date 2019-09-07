from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About, Client, Project, Service


class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['projects'] = Project.objects.all()
        context['clients'] = Client.objects.all()
        return context
