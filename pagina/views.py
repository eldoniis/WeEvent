from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from decimal import Decimal
from .models import *

class HomePage(TemplateView):
    template_name = 'home.html'

class EventIndexView(TemplateView):
    template_name = 'events_index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["events"] = Evento.objects.all()

        return render(request, self.template_name, viewData)
    
class EventShowView(View):
    template_name = 'show_event.html'

    def get(self, request, id):
        viewData = {}
        viewData["title"] = "Title of the view"
        viewData["subtitle"] =  "Subtitle of the view"
        viewData["event"] = get_object_or_404(Evento,pk=id)
        
        return render(request, self.template_name, viewData)
