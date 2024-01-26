from django.urls import path
from django.contrib.auth.decorators import login_required
from login.views import login_user

#from django.contrib.auth.decorators import login_required

#views
from . import views
urlpatterns =[
    path('', views.moderador, name='moderador'),
    path('create',views.create_Post, name='create'),
    path('listar', login_required (views.listar_Post), name='listar'),
    #path('editar_post/<int:post_id>/', editar_post, name='editar_post')

]