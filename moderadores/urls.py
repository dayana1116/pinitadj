from django.urls import path
from django.contrib.auth.decorators import login_required



#from django.contrib.auth.decorators import login_required

#views
from . import views
urlpatterns =[ 
    path('create',views.create_Post, name='create'),
    path('listar', login_required (views.listar_Post), name='listar'),
    path('editar_post/<int:idpost>', login_required (views.update_post), name='editar_post'),
    path('eliminar/<int:idpost>', views.delete_post, name='eliminar_post'),
    


]