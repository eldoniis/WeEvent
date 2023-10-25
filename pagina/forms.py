from django import forms
from .models import Evento, Comentario
 
class ComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentario
        fields = (
            'texto',
            )

    def init(self, args, **kwargs):
        super(ComentarioForm, self).init(args, **kwargs)

        # Campos obligatorios y opcionales
        self.fields['texto'].required = False
        self.fields['texto'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Introduzca su comentario'
        })

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = (
            'nombre',
            'ubicacion',
            'fechaInicio',
            'fechaFin',
            'organizador',
            'descripcion',
            'image_url',
            'videos',
            'precio',
            'capacidad',
            'categorias',
            'etiquetas',
            'esRecurrente',
            'reservas',
            'esDestacado'
            )


    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)

        # Campos obligatorios y opcionales
        self.fields['nombre'].required = True
        self.fields['ubicacion'].required = True
        self.fields['fechaInicio'].required = True
        self.fields['fechaFin'].required = False
        self.fields['organizador'].required = False
        self.fields['descripcion'].required = False
        self.fields['image_url'].required = False
        self.fields['videos'].required = False
        self.fields['precio'].required = False
        self.fields['capacidad'].required = False
        self.fields['categorias'].required = False
        self.fields['etiquetas'].required = False
        self.fields['esRecurrente'].required = False
        self.fields['reservas'].required = False
        self.fields['esDestacado'].required = False

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre del evento'
        })
        self.fields['ubicacion'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ubicación del evento'
        })
        self.fields['fechaInicio'].widget.attrs.update({
            'class': 'form-control datepicker',
            'placeholder': 'Fecha de inicio (YYYY-MM-DD)'
        })
        self.fields['fechaFin'].widget.attrs.update({
            'class': 'form-control datepicker',
            'placeholder': 'Fecha de finalización (YYYY-MM-DD)'
        })
        self.fields['organizador'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Organizador del evento'
        })
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descripción del evento'
        })
        self.fields['image_url'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'URL de la imagen del evento (https://www.imagen...)'
        })
        self.fields['videos'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'URL del video del evento (https://www.video...)'
        })
        self.fields['precio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Precio del evento'
        })
        self.fields['capacidad'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Capacidad del evento'
        })
        self.fields['categorias'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Categorías del evento'
        })
        self.fields['etiquetas'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Etiquetas del evento'
        })
        self.fields['esRecurrente'].widget.attrs.update({
            'class': 'form-check-input',
        })
        self.fields['esRecurrente'].label = '¿El evento es recurrente?'

        self.fields['reservas'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Reservación del evento'
        })
        self.fields['esDestacado'].widget.attrs.update({
            'class': 'form-check-input',
        })
        self.fields['esDestacado'].label = '¿El evento es destacado?'