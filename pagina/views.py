from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.views import View
from django import forms
from decimal import Decimal
from .models import *
from .forms import *

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
    
class CreateEventView(View):
    template_name = 'create_event.html'

    def get(self, request):
        form = EventoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            return redirect('show_event', id=evento.id)
        return render(request, self.template_name, {'form': form})
    
class DeleteEventView(View):
    def get(self, request, id):
        evento = get_object_or_404(Evento, id=id)
        evento.delete()
        return redirect('events_index')
