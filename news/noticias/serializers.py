from rest_framework import serializers
from .models import *

class EventosSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	nombre = serializers.CharField()
	fecha = serializers.DateTimeField(read_only = True)
	descripcion = serializers.CharField()
	imagen = serializers.CharField()

	def create(self,validated_data):
		return Eventos.objects.create(**validated_data)

class UsuariosSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	matricula = serializers.CharField()
	nombre = serializers.CharField()

	def create(self,validated_data):
		return Usuarios.objects.create(**validated_data)

class NoticiasSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	categoria = serializers.CharField()
	titulo = serializers.CharField()
	pub_date = serializers.DateTimeField(read_only = True)
	descripcion = serializers.CharField()
	imagen = serializers.CharField()

	def create(self,validated_data):
		noticias = Noticias()
		noticias.categoria = Categoria.objects.all().get(nombre=validated_data['categoria'])
		noticias.titulo = validated_data['titulo']
		noticias.descripcion = validated_data['descripcion']
		noticias.imagen = validated_data['imagen']
		noticias.save()
		return noticias
		

class CatogoriaSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	nombre = serializers.CharField()
	
	def create(self,validated_data):
		return Categoria.objects.create(**validated_data)