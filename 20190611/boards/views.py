from django.shortcuts import render, redirect
from .models import Board, Comment

def index(request):
    boards = Board.objects.order_by('-pk')
    # boards = Board.objects.all()[::-1]
    context = {'boards':boards}
    return render(request, 'boards/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = Comment.objects.get(pk=board_pk)
    context = {'board':board, 'comments':comments}
    return render(request, 'boards/detail.html', context)

def edit(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board':board}
        return render(request, 'boards/edit.html', context)

def delete(request, board_pk):
    if request.method == 'POST':
        board = Board.objects.get(pk=board_pk)
        board.delete()
        return redirect('boards:index')
    else:
        return render(request, 'boards/detail.html')

def comments_create(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        comment = Comment()
        # comment.board = board
        comment.board_id = board.pk
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)