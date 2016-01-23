from django import forms
from django.forms import ModelForm
from .models import *
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib



class EventoForm(forms.ModelForm):

        class Meta:
            model = Eventos
            fields = ('nombre', 'descripcion', 'imagen')

class NoticiaForm(forms.ModelForm):

        class Meta:
            model = Noticias
            #fields = ('categoria', 'titulo', 'descripcion' ,'imagen')
            fields = '__all__'

            

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class PhotoDirectForm(NoticiaForm):
    image = CloudinaryJsFileField()

#class PhotoDirectForm(PhotoForm):
#    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(NoticiaForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
