from django.urls import path


#views
from . import views
urlpatterns =[
    path('', views.login, name='login'),
    path('logout',views.logout_user, name='logout')
] 