from django.db import models
from django.utils import timezone
import cloudinary
import cloudinary.uploader
import cloudinary.api	
from cloudinary.models import CloudinaryField

class Eventos(models.Model):
	nombre = models.CharField(max_length=200)
	fecha = models.DateTimeField('Fecha del evento',default=timezone.now)
	descripcion = models.TextField()
	imagen = models.CharField(max_length=1000)
	def __str__(self):
		return '%s' % (self.nombre)


class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return '%s' % (self.nombre)

class Noticias(models.Model):
	categoria = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Fecha de Publicacion',default=timezone.now)
	descripcion = models.TextField()
	imagen = models.CharField(max_length=1000)
	title = models.CharField("Title (optional)", max_length=200, blank=True)
	image = CloudinaryField('image') 

	def __str__(self):
		return '%s' % (self.titulo)
	
class Usuarios(models.Model):
	matricula = models.CharField(max_length=100, primary_key=True)
	nombre = models.CharField(max_length=200)
	password = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.nombre)


class Photo(models.Model):
    ## Misc Django Fields
    
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)

    ## Points to a Cloudinary image
    image = CloudinaryField('image')

    """ Informative name for mode """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)