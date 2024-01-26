from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import PostForm
from django.http import JsonResponse
#from django.shortcuts import get_object_or_404
from .models import Post

def moderador(request):
    return render(request,'controlBlog.html') 


# Create your views here.
def create_Post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos insertados correctamente.')
            return redirect('listar')
        else:
            messages.error(request, 'Error al insertar datos. Revise los datos.')
            messages.error(request, form.errors)
    else:
        form = PostForm()

    return render(request, 'controlBlog.html', {'form': form})

#listar los post
def listar_Post(request):
    posts = Post.objects.all()
    return render(request, 'controlBlog.html', {"posts": posts})

#operacion para modificar un post

