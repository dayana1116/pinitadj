from django.shortcuts import render


# Create your views here.
def single(request):
    return render(request, 'single.html')