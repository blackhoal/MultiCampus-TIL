from django.shortcuts import render

def index(request):
    return render(request, 'boards/index.html')

def new(request):
    return render(request, 'boards/new.html')

def create(request):
    title - request.POST.get('title')
    content = request.POST.get('content')

    board = Board()
    board.save()
    return redirect('/boards/')