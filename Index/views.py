from django.shortcuts import render
from .models import Post
#from moderadores.views import vista_post,single_post

# Create your views here.
def index(request):
    return render(request, 'index.html')

# esta funcion sirve para mostrar los post la parte del blogpost en la parte de la interfaz para el usuario
def vista_post(request,idpost):
    ##posts = Post.objects.all()  # Obtener todos los posts de la base de datos

    post = Post.objects.filter(idpost=idpost).first()
    return render(request, 'index.html', {'posts': post})

# con esta funcion se visualizara solo un id del post
def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'single.html', {'post': post})
    

