from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post
from .forms import Registropost

# Create your views here.
def moderador(request):
    return render(request,'controlBlog.html')

class Registrarpost(CreateView):
    model = Post
    form_class = Registropost
    template_name = 'moderador/controlBlog.html'

