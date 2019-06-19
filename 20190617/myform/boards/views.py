from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm # 20190617
from IPython import embed # 20190617

def index(request):
    boards = Board.objects.all()[::-1]
    # boards = Board.objects.order_by('-id')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST) # 20190617
        # embed() 주석처리 안할 경우 계속 해당 구문에서 멈춤
        if form.is_valid(): # 유효성 검사 메소드 / form의 유효성이 False일 경우 25줄로 넘어간다
            title = form.cleaned_data.get('title') # 사용할 수 있는 형태로 정제 후 데이터를 딕셔너리 형태(form.cleaned_data - 딕셔너리)로 추출
            # title = request.POST.get('title')
            content = form.cleaned_data.get('content')
            board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form} # if, else문과 동일한 위치
    # 위의 form과 아래의 form의 차이는 오류 내용이 들어있는가
    return render(request, 'boards/create.html', context)

def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk) # 해당되는 object가 있을 경우 정상적으로 가져오고, 없을 경우 404 오류를 출력
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
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            # board = Board.objects.set(title=title, content=content) # 쿼리 복잡 수행시간 늘어남
            board.save()
            return redirect('boards:detail', board_pk)
    else:
        form = BoardForm(initial=board.__dict__) # 뉴는 폼만 제공 어떤 것을 만들었는지 / 밸류 지정이랑 동일
    context = {'form': form}
    return render(request, 'boards/create.html', context)
