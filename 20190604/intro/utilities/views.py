from django.shortcuts import render

def index(request):
    return render(request, 'utilities/index.html')

def images(request):
    return render(request, 'utilities/images.html')