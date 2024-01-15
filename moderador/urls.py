from django.urls import path
from django.contrib.auth.decorators import login_required

#views
from . import views
urlpatterns =[
    path('', views.moderador, name='moderador'),

]