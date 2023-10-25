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

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["events"] = Evento.objects.all()
    viewData["contador"] = 0
    for event in viewData["events"]:
        if event.ubicacion == User.location:
            viewData["contador"] = viewData["contador"] + 1

    return render(request, template_name, viewData)

@login_required
def ShowProfile(request):
    template_name = 'profile.html'

    viewData = {}
    viewData["subtitle"] =  "User Profile"

    return render(request,template_name, viewData)

@login_required
def EventIndexView(request):
    template_name = 'events_index.html'

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Eventos"
    viewData["events"] = Evento.objects.all()

    return render(request, template_name, viewData)

@login_required
def EventShowView(request,id):
    template_name = 'show_event.html'

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Info Eventos"
    viewData["event"] = get_object_or_404(Evento,pk=id)
        
    return render(request, template_name, viewData)

@login_required
def CreateEventView(request):
    template_name = 'create_event.html'

    if request.method == 'POST':
        form = EventoForm(request.POST)

        if form.is_valid():
            # El formulario es válido, guarda el evento y redirige a la página de detalles
            evento = form.save()
            return redirect('events_index')
        else:
            # El formulario no es válido, muestra los errores en el formulario
            print(form.errors)
    else:
        form = EventoForm()
    
    return render(request, template_name, {'form': form})
        
@login_required
def DeleteEventView(request,id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('events_index')

@login_required
def DeleteUser(request,id):
    user = get_object_or_404(User, id=id)
    user.delete()
    
    return redirect('home')

@login_required
def Support(request):
    template_name = 'support.html'
    viewData = {}
    viewData["subtitle"] =  "User Support"

    return render(request,template_name,viewData)