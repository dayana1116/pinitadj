from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import PostForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
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
def update_post(request, idpost): #obtener los datos del post mediante el id
    post = get_object_or_404(Post, idpost=idpost)
    if request.method == 'POST': #revisa si la solicitud es post y puede enviar los nuevos datos
        form = PostForm(request.POST,request.FILES, instance=post) #se crea el formulario para la validacion
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.save()
            form.save()#si son validos se guardan 
            data = {'message': 'Datos actualizados correctamente'} 
            return redirect('listar') #se regresa al la pagina donde estan los post
        else:
            data = {'error': 'Error al actualizar datos. Revise los datos.'}
            return JsonResponse(data)
    else:
        data = {
            'titulo':post.titulo,
            'contenido':post.contenido,
            'extracto':post.extracto,
            
        }
        
        return JsonResponse(data)#toma los datos almacenado y los envia  a donde se ralizo la solicitud

@csrf_exempt # desactiva la protección CSRF para que se pueda eliminar registros
def delete_post(request, idpost):
    
            post = get_object_or_404(Post, idpost=idpost) 
            post.delete()
            return JsonResponse({'message': 'Post eliminado correctamente'})


        

