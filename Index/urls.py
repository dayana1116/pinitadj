from django.urls import path
from .views import index

#views
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('', index, name='index'),
    path('posts/', views.vista_post, name='vista_post'),
    path('post/<int:post_id>/', views.single_post, name='single_post'),


]
