from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm, CommentForm # 20190617
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    boards = Board.objects.all()[::-1]
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

@login_required() # 190619 추가
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False) # 190619 추가
            board.user = request.user # 190619 추가
            board.save() # 190619 추가
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
    comments = board.comment_set.all() # 190619 추가
    comment_form = CommentForm()
    context = {
        'board': board,
        'comments': comments, # 190619 추가
        'comment_form': comment_form # 190619 추가
               }
    return render(request, 'boards/detail.html', context)

def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board_pk)
    else:
        return redirect('board:index')

@login_required() # 190619 추가
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        if request.method =='POST':
            form = BoardForm(request.POST, instance=board) # 20190618 instance 추가
            if form.is_valid():
                board.save()
                return redirect('boards:detail', board_pk)
        else:
            form = BoardForm(instance=board) # 20190618 initial 대신 instance 추가
    else:
        return redirect('board:index')
    context = {'form': form, 'board': board}
    return render(request, 'boards/form.html', context)

@login_required()
@require_POST # POST를 제외한 다른 요청이 들어올 시 405에러 출력
def comments_create(request, board_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    return redirect('boards:detail', board_pk)

@login_required()
@require_POST
def comments_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('boards:detail', board_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)
