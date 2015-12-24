from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *


def evento_nueva(request):
        if request.method == "POST":
		form = EventoForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'noticias/base2.html',{})
	else:
		form = EventoForm()
	return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Evento'})

def noticia_nueva(request):
	if request.method == "POST":
		form = NoticiaForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'noticias/base2.html',{})
	else:
		form = NoticiaForm()
	return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Noticia'})


def evento_edit(request,pk):
		post = get_object_or_404(Eventos, pk=pk)
		if request.method == "POST":
			form = EventoForm(request.POST, instance=post)
			if form.is_valid():
				form.save
				return redirect('noticias.views.post_detail', pk=post.pk)
		else:
			form = EventoForm(instance=post)
		return render(request, 'noticias/evento_detail.html', {'form': form, 'post' : post})

#def noticia_edit(request):