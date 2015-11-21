from django.db import models

class Eventos(models.Model):
	nombre = models.CharField(max_length=200)
	fecha = models.DateTimeField('Fecha del evento')
	descripcion = models.CharField(max_length=1000)

class Categoria(models.Model):
	nombre = models.CharField(max_length=200)

class Noticias(models.Model):
	categoria = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Fecha de Publicacion')
	descripcion = models.CharField(max_length=2000)
	
class Usuarios(models.Model):
	matricula = models.CharField(max_length=100, primary_key=True)
	nombre = models.CharField(max_length=200)
	password = models.CharField(max_length=100)

	#prueba