"""pinitadj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth.views import LoginView
#, logout_then_login

 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('Index.urls')),
    path('moderador/',include('moderador.urls')),
   # path('login/',include('login.urls')),
    path('fundacion/',include('Fundacion.urls')),
    path('registro/',include('registro.urls')),
    path('contacto/',include('contacto.urls')),
    path('single/',include('single.urls')),
    path('', LoginView.as_view(template_name='formlogin.html'), name='Login'),
    
]
