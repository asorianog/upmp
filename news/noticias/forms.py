from django import forms
from .models import *

class EventoForm(forms.ModelForm):

        class Meta:
            model = Eventos
            fields = ('nombre', 'descripcion', 'imagen')

class NoticiaForm(forms.ModelForm):

        class Meta:
            model = Noticias
            fields = ('categoria', 'titulo', 'descripcion' ,'imagen')