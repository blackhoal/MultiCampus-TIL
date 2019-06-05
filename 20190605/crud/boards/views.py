from django.shortcuts import render
from .models import Board

def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    board = Board(title=title, content=content)
    board.save()
    return render(request, 'boards/create.html')