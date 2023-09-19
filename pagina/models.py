from django.db import models
from django.utils.translation import gettext_lazy as _

class Evento(models.Model):
    class Tipo(models.TextChoices):
        depo='deportes',_('deportes')
        cult='cultural',_('cultural')
        mus='musical',_('muscial')
        gastr='gastronomico',_('gastronomico')
    nombre=models.CharField(max_length=30)
    capacidad=models.CharField(max_length=4)
    tipoDePrenda=models.CharField(default='' , max_length=40)
    tipo =models.CharField(max_length=13,choices=Tipo.choices,default=Tipo.depo)
    descripcion=models.TextField
    image=models.ImageField(upload_to='pagina/images', default='')
    

    
    
