from django.urls import path

#views
from . import views
urlpatterns =[
    path('', views.registro, name='registro')
]