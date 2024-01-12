from django import forms
from django.forms import ModelForm
from .models import Post

class Registropost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['idpost', 'titulo', 'contenido', 'imagen', 'tipoimagen', 'fecha', 'autor', 'extracto']
