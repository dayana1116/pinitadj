from django.urls import path
from .views import index

#views
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('', index, name='index')

]
