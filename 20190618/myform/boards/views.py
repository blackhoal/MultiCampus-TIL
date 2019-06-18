from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm # 20190617


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # 20190618 주석 처리
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            board = form.save() # 20190618 Model Form
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form} # if, else문과 동일한 위치
    # 위의 form과 아래의 form의 차이는 오류 내용이 들어있는가
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    # board = Board.objects.get(pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board_pk)

def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method =='POST':
        form = BoardForm(request.POST, instance=board) # 20190618 instance 추가
        if form.is_valid():
            board.save()
            return redirect('boards:detail', board_pk)
    else:
        form = BoardForm(instance=board) # 20190618 initial 대신 instance 추가
    context = {'form': form, 'board': board}
    return render(request, 'boards/form.html', context)
