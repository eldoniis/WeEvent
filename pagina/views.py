from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
import folium

def HomePage(request):
    template_name = 'home.html'
    initialMap = folium.Map(location=[6.2438171,-75.5747339], zoom_start=15)

    viewData = {}
    viewData["title"] = "Title of the view"
    viewData["subtitle"] =  "Subtitle of the view"
    viewData["events"] = Evento.objects.all()
    viewData["map"] = initialMap._repr_html_()

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
            event = form.save()
            messages.success(request,'Evento creado correctamente')
            return redirect('events_index')
        else:
            # El formulario no es válido, muestra los errores en el formulario
            print(form.errors)
    else:
        form = EventoForm()
    
    return render(request, template_name, {'form': form})

@login_required
def asistencia(request,id):

    post = get_object_or_404(Evento,id=id)
    if request.user in post.asistencia.all():

        post.asistencia.remove(request.user)
    else:
        post.asistencia.add(request.user.id)


    return redirect('events_index')
        
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

@login_required
def darLike(request,id):
    post = get_object_or_404(Evento,id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)

    return redirect('events_index')

@login_required
def comentario(request,id):
    template_name = 'comentar.html'
    print(ComentarioForm(request.POST))
    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            # El formulario es válido, guarda el evento y redirige a la página de detalles
            form = form.save()
            return redirect('events_index')
        else:
            # El formulario no es válido, muestra los errores en el formulario
            print(form.errors)
    else:
        form = ComentarioForm()
    
    return render(request, template_name, {'form': form})