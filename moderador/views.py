from django.shortcuts import render, redirect
from django import forms
from .models import Post
from .forms import Registropost

# Create your views here.
def moderador(request):
    return render(request,'controlBlog.html')
