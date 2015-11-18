from rest_framework import serializers
from .models import *

class EventosSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	nombre = serializers.CharField()
	fecha = serializers.DateTimeField()
	descripcion = serializers.CharField()

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
	titulo = serializers.CharField()
	pub_date = serializers.DateTimeField()
	descripcion = serializers.CharField()

	def create(self,validated_data):
		return Noticias.objects.create(**validated_data)

class CatogoriaSerializers(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	nombre = serializers.CharField()
	
	def create(self,validated_data):
		return Categoria.objects.create(**validated_data)
