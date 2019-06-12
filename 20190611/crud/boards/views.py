from django.shortcuts import render, redirect
from .models import Board

def index(request):
    # boards = Board.objects.order_by('-id')
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board(title=title, content=content)
        board.save()
        return redirect('create', board.pk)  # 20190611
    else:
        return render(request, 'boards/new.html')

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect('delete')
    else:
        return render(request, 'boards/detail.html')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)  # 20190611
    else:
        context = {'board': board}
        return render(request, 'boards/edit.html', context)

