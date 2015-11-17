from .models import *

from .serializers import *

from rest_framework import viewsets

class EventosViewSet(viewsets.ModelViewSet):
	serializer_class = EventosSerializers
	queryset = Eventos.objects.all()

class UsuariosViewSet(viewsets.ModelViewSet):
	serializer_class = UsuariosSerializers
	queryset = Usuarios.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
	serializer_class = CatogoriaSerializers
	queryset = Categoria.objects.all()

class NoticiasViewSet(viewsets.ModelViewSet):
	serializer_class = NoticiasSerializers
	queryset = Noticias.objects.all()