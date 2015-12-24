from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm

def post_new(request):
	return render(request, 'noticias/base2.html',{})

	'''
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('noticias.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'noticias/post_edit.html', {'form': form})
        '''