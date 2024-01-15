from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
    return render(request,'formlogin.html') 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario es autenticado, iniciar sesión
            login(request, user)
            return redirect('moderador')
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