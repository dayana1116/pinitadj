from django import forms
from .models import Post

class PostForm (forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [ 'titulo', 'contenido','extracto',]
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
                


