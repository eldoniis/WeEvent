from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django import forms

class CategoriaInteresForm(forms.ModelForm):
   
   class Meta:
        model = User
        fields = 'CategoriaInteres',
   
   OPTIONS = (
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

   CategoriaInteres = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'age', 'location', 'role','password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})