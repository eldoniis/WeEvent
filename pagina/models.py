from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    fechalnicio = models.DateField()
    fechaFin = models.DateField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagenes = models.ImageField(upload_to='event_images/')
    videos = models.URLField()
    precio = models.FloatField()
    capacidad = models.IntegerField()
    asistencia = models.IntegerField()
    categorias = models.CharField(max_length=255)
    etiquetas = models.CharField(max_length=255)
    esRecurrente = models.BooleanField()
    reservas = models.ManyToManyField(User, related_name='reservas')
    calificacion = models.FloatField()
    comentarios = models.ManyToManyField(User, through='Comentario')
    esDestacado = models.BooleanField()

    def actualizarEvento(self):
        # Lógica para actualizar el evento
        pass

    def crearEvento(self):
        # Lógica para crear un nuevo evento
        pass

    def eliminarEvento(self):
        # Lógica para eliminar el evento
        pass

    def reservar(self, usuario):
        # Lógica para permitir que un usuario haga una reserva en el evento
        pass

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto

    

    
    
