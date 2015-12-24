from django.db import models
from django.utils import timezone

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

	def __str__(self):
		return '%s' % (self.titulo)
	
class Usuarios(models.Model):
	matricula = models.CharField(max_length=100, primary_key=True)
	nombre = models.CharField(max_length=200)
	password = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.nombre)