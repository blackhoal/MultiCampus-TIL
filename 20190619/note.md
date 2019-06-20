요약
- 인증 권한(회원 가입/글 작성/댓글 작성&삭제)	
- git commit -m "190619 Authentication"

1. 비밀번호 변경 기능
	- accounts - views.py
	- 모듈 import
	from django.contrib.auth.forms import PasswordChangeForm
	- change_password 메소드 추가
	- 유저의 인증정보가 불일치하므로 자동으로 로그아웃됨
	-> 해당 구문 추가시 비밀번호를 변경해도 로그인 상태 유지
	from django.contrib.auth import update_session_auth_hash
	
	if form.is_valid():
	    user = form.save()
	    update_session_auth_hash(request, user)
	    form.save()
	    return redirect('boards:index')
	
2. 권한이 있는 사용자만 글을 작성할 수 있도록 하는 기능
	- Boards - views.py
	from django.contrib.auth.decorators import login_required
	
	@login_required()
	def create(request):
	
	@login_required()
	def update(request, board_pk):
	- 로그인하지 않은 사용자가 글을 작성 시 로그인 페이지로 이동
	- 문제 : 위의 과정에서 로그인하면 index 페이지로 이동되는데 index 페이지가 아니라 글 작성페이지로 이동을 원함
	-> accounts - views.py
	def login(request):
	            ~	
	            return redirect(request.GET.get('next') or 'boards:index')
	
3. 4개의 html을 하나의 html로 병합(signup.html, edit.html, login.html, change_password.html)
	- auth_form.html 생성(기존의 change_password.html 내용 복사) 및 코드 추가
	{% extends 'boards/base.html' %}
	{% load bootstrap4 %}
	
	{% block body %}
	{% if request.resolver_match.url_name == 'signup' %}
	    <h1>회원 가입</h1>
	{% elif request.resolver_match.url_name == 'login' %}
	    <h1>로그인</h1>
	{% elif request.resolver_match.url_name == 'edit' %}
	    <h1>회원정보 수정</h1>
	{% else %}
	    <h1>비밀번호 변경</h1>
	{% endif %}
	<form action="" method="post">
	    {% csrf_token %}
	    {% bootstrap_form form %}
	    {% buttons %}
	        <button type="submit" class="btn btn-primary">Submit</button>
	    {% endbuttons %}
	</form>
	{% endblock%}
	
	- views.py 수정
	def login(request):
	    ~
	    return render(request, 'accounts/auth_form.html', context)
	
	def edit(request):
	    ~
	    return render(request, 'accounts/auth_form.html', context)
	
	def change_password(request):
	    ~
	    return render(request, 'accounts/auth_form.html', context) 
	
	- 4개의 html 삭제 (signup.html, edit.html, login.html, change_password.html)
	
4. 1:N 관계
	- 게시글(1) : 댓글(N)
	게시글이 삭제될 경우 댓글 또한 전체 삭제
	- 유저(1) : 게시글(N)
	유저의 계정이 삭제될 경우 게시글 또한 전체 삭제
	- Boards-models.py~
	from django.conf import settings
	
	class Board(models.Model):
	    ~
	    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	- $ python manage.py makemigrations
	Select an option : 1 & enter - 1 & enter
	- $ python manage.py migrate
	# NOT NULL constraint failed: Board_board.user_id 오류 발생
	-> models.py에서 정의한 
	- boards - views.py 코드 추가
	def create(request):
	    if request.method == 'POST':
	        form = BoardForm(request.POST)
	        if form.is_valid():
	            board = form.save(commit=False)
	            board.user = request.user
	            board.save()
	- boards-index.html
	{% extends 'boards/base.html' %}
	{% block body %}
	    <h1>INDEX</h1>
	    <hr>
	    {% for board in boards %}
	        <p><b>작성자: {{ board.user}}</b></p>
	        <p>글 번호: {{ board.pk }}</p>
	        <p>글 제목: {{ board.title }}</p>
	- boards-detail.html
	{% if user == board.user %}
	    <a href="{% url 'boards:update' board.pk %}">[수정]</a>
	    <form action="{% url 'boards:delete' board.pk %}" method="POST">
	        {% csrf_token %}
	        <input type="submit" value="글 삭제">
	    </form>
	{% endif %}
	- boards-views.py 
	def update(request, board_pk):
	    board = get_object_or_404(Board, pk=board_pk)
	    if board.user == request.user:
	        if request.method =='POST':
	            form = BoardForm(request.POST, instance=board)
	            if form.is_valid():
	                board.save()
	                return redirect('boards:detail', board_pk)
	        else:
	            form = BoardForm(instance=board)
	    else:
	        return redirect('boards:index')
	    context = {'form': form, 'board': board}
	    return render(request, 'boards/form.html', context)
	-> 코드에 대한 해석 : board.user와 request.user가 일치하지 않을 경우 index 페이지로 이동
	
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
	
현재 접속중인 사용자(request.user)와 글의 작성자(board.user)가 동일할 경우 수정 버튼 활성화

![1](.\images\1.png)

![2](.\images\2.png)

5. 댓글 기능
	- Boards-models.py 코드 추가
	class Board(models.Model):
	    title = models.CharField(max_length=20)
	    content = models.TextField()
	    created_at = models.DateTimeField(auto_now_add=True)
	    updated_at = models.DateTimeField(auto_now=True)
	    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	class Comment(models.Model):
	    content = models.CharField(max_length=100)
	    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	    board = models.ForeignKey(Board, on_delete=models.CASCADE)
# 구문 해석
board = models.ForeignKey(Board, on_delete=models.CASCADE) 
	○ 내부 구성
		Comment(클래스)
		id,content,board_id (양식)
		(1, a, 3) -> 3번 게시글의 내용 'a'를 가지는 1번 댓글
		(2, s, 3) -> 3번 게시글의 내용 's'를 가지는 2번 댓글
		(3, d, 4) -> 4번 게시글의 내용 'd'를 가지는 3번 댓글
		(4, f, 4) -> 4번 게시글의 내용 'f'를 가지는 4번 댓글
		○ ForeignKey : 외래키 참조
		○ Board : 위에 순차적으로 정의된 Board 클래스 -> Board를 참조하므로 Board보다 먼저 정의되면 X
		○ settings.AUTH_USER_MODEL : Django가 기본적으로 가지고 있는 모델 / String 형태
		○ on_delete=models.CASCADE : 게시글이 삭제 시 참조한 board의 내용 또한 전체 삭제됨을 의미
	- $ python manage.py makemigrations
	- $ python manage.py migrate
	- boards-forms.py
	from .models import Board, Comment
	
	class CommentForm(forms.ModelForm):
	    class Meta:
	        model = Comment
	        fields = ['content', ]
	- boards - admin.py
	from .models import Board, Comment
	
	class CommentAdmin(admin.ModelAdmin):
	    list_display = ('content',)
	    
	admin.site.register(Comment, CommentAdmin)
	- boards - views.py 코드 추가
# 댓글을 출력하는 방식 2가지
		a. html
		{% for comment in board.comment_set.all %}
		{{ comment.content }}
		{% endfor %}
		{% if user == board.user %}
		
		b. comments = board.comment_set.all() -> 해당 방식 채택
		from .forms import BoardForm, CommentForm
		from django.views.decorators.http import require_POST
		
		def detail(request, board_pk):
		    board = get_object_or_404(Board, pk=board_pk)
		    comments = board.comment_set.all()
		    comment_form = CommentForm()
		    context = {
		        'board': board,
		        'comments': comments,
		        'comment_form': comment_form
		               }
		    return render(request, 'boards/detail.html', context)
		
		@login_required()
		def comment_create(request, board_pk):
		    comment_form = CommentForm(request.POST)
		    if comment_form.is_valid():
		        comment = comment_form.save(commit=False)
		        comment.user = request.user
		        comment.board_id = board_pk
		        comment.save()
		    return redirect('boards:detail', board_pk)
		# require_POST
		  -> POST를 제외한 다른 요청이 들어올 시 405에러 출력
	- urls.py
	urlpatterns = [
	    ~
	    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
	]

6. 로그인한 사용자만 댓글 작성이 가능하도록 하는 기능
	- detail.html
	    <h3>댓글 작성</h3>
	    {% if user.is_authenticated %}
	        <form action="{% url 'boards:comments_create' board.pk %}" method="POST">
	            {% csrf_token %}
	            {{ comment_form.as_p }}
	            <input type="submit" value="댓글 작성">
	        </form>
	        <hr>
	    {% else %}
	        <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인을 해주세요]</a><br>
	    {% endif %}
	
7. 댓글 삭제
	- boards - views.py
	from .models import Board, Comment
	
	@login_required()
	@require_POST
	def comments_delete(request, board_pk, comment_pk):
	    comment = get_object_or_404(Comment, pk=comment_pk)
	    if request.user != comment.user:
	        return redirect('boards:detail', board_pk)
	comment.delete()
	    return redirect('boards:detail', board_pk)
	
	- detail.html
	    <h3>댓글</h3>
	    {% for comment in comments|dictsortreversed:'pk' %}
	        <p><b>{{ comment.user }}님의 댓글: {{ comment.content}}</b></p>
	        {% if comment.user == user %}
	            <form action="{% url 'boards:comments_delete' board.pk %}">
	                {% csrf_token %}
	                <input type="submit" value="댓글 삭제">
	            </form>
	            <hr>
	        {% endif %}
	    {% empty %}
	        <p><b>댓글이 없습니다.</b></p>
	    {% endfor%}
	※ {% for comment in comments|dictsortreversed:'pk' %}  구문 해석
		- 앞의 구문에 이어(파이프 라인) 딕셔너리 목록을 가져와 pk를 기준으로 정렬된 목록을 역순으로 반환
	
8. a 태그와 form 태그의 차이
	-   a 태그    : get 메소드만 사용 가능
	form 태그 : get/post 메소드 둘다 사용 가능
	- Get/post 메소드 사용 구분
		○ DB에 대한 조작이 필요한 경우 Post 메소드 사용
