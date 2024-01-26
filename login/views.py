from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
""" def login(request):
    return render(request,'formlogin.html') 
 """
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es autenticado, iniciar sesión
            login(request, user)
            if user.is_staff and user.is_superuser:
                #el usuariio es un miembro del grupo moderador
                print("redireccionando a controlBlog para moderador")
                return redirect('controlBlog')
        else:
            # El usuario no es autenticado, mostrar un mensaje de error
            messages.error(request, 'El nombre de usuario o contrseña no son correctos.')
            return redirect('login')
    else:
        return render(request, 'formlogin.html')
def logout_user(request):
    # Cerrar sesión del usuario
    logout(request)
    return redirect('login')

""" def registro(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

    if not User.objects.filter(username=username).exists():
        #crea un nuevo usuario
        User = User.objects.create_user(username=username,password=password)
 """