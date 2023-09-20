from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import View
from django import forms
from decimal import Decimal
from .models import *
from .forms import *

def HomePage(request):
    template_name = 'home.html'

    return render(request, template_name)

@login_required
def EventIndexView(request):
    template_name = 'events_index.html'

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["events"] = Evento.objects.all()

    return render(request, template_name, viewData)
    
def EventShowView(request,id,):
    template_name = 'show_event.html'

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["event"] = get_object_or_404(Evento,pk=id)
        
    return render(request, template_name, viewData)
    
def CreateEventView(request):
    template_name = 'create_event.html'

    form = EventoForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        evento = form.save()
        return redirect('show_event', id=evento.id)
        
    
    return render(request, template_name, {'form': form})

def DeleteEventView(request,id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('events_index')