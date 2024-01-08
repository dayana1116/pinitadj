from django.shortcuts import render

# Create your views here.
def moderador(request):
    return render(request,'controlBlog.html')
