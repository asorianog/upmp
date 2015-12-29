from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect

def evento_list(request):
	posts = Eventos.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
        return render(request, 'noticias/evento_list.html', {'posts': posts})

def noticia_list(request):
	posts = Noticias.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
        return render(request, 'noticias/noticia_list.html', {'posts': posts})

def evento_nueva(request):
        if request.method == "POST":
		form = EventoForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('noticias.views.evento_detail', pk=post.pk)
	else:
		form = EventoForm()
	return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Evento'})

def noticia_nueva(request):
	if request.method == "POST":
		form = NoticiaForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('noticias.views.noticia_detail', pk=post.pk)
	else:
		form = NoticiaForm()
	return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Noticia'})

def evento_detail(request, pk):
        post = get_object_or_404(Eventos, pk=pk)
        return render(request, 'noticias/evento_detail.html', {'post': post, 'tipo' : 'Evento'})

def noticia_detail(request, pk):
        post = get_object_or_404(Noticias, pk=pk)
        return render(request, 'noticias/noticia_detail.html', {'post': post, 'tipo' : 'Noticia'})

def evento_edit(request,pk):
		post = get_object_or_404(Eventos, pk=pk)
		if request.method == "POST":
			form = EventoForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
				return redirect('noticias.views.evento_detail', pk=post.pk)
		else:
			form = EventoForm(instance=post)
		return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Evento', 'post' : post})

def noticia_edit(request,pk):
		post = get_object_or_404(Noticias, pk=pk)
		if request.method == "POST":
			form = NoticiaForm(request.POST, instance=post)
			if form.is_valid():
				form.save()
				return redirect('noticias.views.noticia_detail', pk=post.pk)
		else:
			form = NoticiaForm(instance=post)
		return render(request, 'noticias/post_edit.html', {'form': form, 'tipo' : 'Noticia', 'post' : post})