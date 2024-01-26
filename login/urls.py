#configuracion de urls de está app
from django.urls import path

#views
from . import views
urlpatterns =[
    path('',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout')
    
]