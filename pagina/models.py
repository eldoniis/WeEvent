from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User

class Evento(models.Model):
    categorias = (
        ("Deportivo","Deportivo"),
        ("Musical","Musical"),
        ("Gastronomico","Gastronomico"),
        ("Cultural","Cultural"),
        ("Ayuda Social","Ayuda Social"),
        ("Mascotas","Mascotas"),
        ("Academico","Academico"),
        ("Tecnologico","Tecnologico"),
        ("CompraVenta","CompraVenta")
        )

    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    image_url = models.URLField()
    videos = models.URLField()
    precio = models.FloatField()
    capacidad = models.IntegerField()
    asistencia = models.ManyToManyField(User, related_name='asistencia')
    categorias = models.CharField(max_length=255, choices=categorias, default="")
    etiquetas = models.CharField(max_length=255)
    esRecurrente = models.BooleanField()
    reservas = models.ManyToManyField(User, related_name='reservas')
    # comentarios = models.ManyToManyField(User, through='Comentario')
    esDestacado = models.BooleanField()
    likes = models.ManyToManyField(User,related_name='evento_likes')

    def cantidad_asistencia(self):
        return self.asistencia.count()
    
    def cantidad_likes(self):
        return self.likes.count()

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
    texto = models.CharField(max_length=255,blank=True,default='')
    fecha = models.DateTimeField(auto_now_add=True)

    def str(self):
        len_tittle = 15
        if len(self.texto) > len_tittle:
            return self.texto[:len_tittle] + '...'
        return self.texto


    class Meta:
        ordering = ['-fecha']    

    
    
