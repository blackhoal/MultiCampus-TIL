요약
- Model Relation

models.py -> 모델 클래스
forms.py -> 모델 폼

1. 진행
- $ django-admin startproject modelrelation
- $ cd crud(프로젝트명)
- $ python manage.py startapp onetomany
modelrelation-settings.py의 INSTALLED_APPS에 등록(onetomany, django_extensions)

![1](.\images\1.png)

- onetomany-models.py에서 3개의 클래스 정의(User, Board, Comment)
※ 유저 & 게시글, 유저 & 댓글, 게시글 & 댓글의 관계를 1 : N의 관계로 생성 
-> models.ForeignKey 사용
- $ python manage.py makemigrations
- $ python manage.py migrate
- http://bit.do/onetomany-haha 해당 구문 복사
user1 = User.objects.create(name='Kim')
user2 = User.objects.create(name='Lee')
board1 = Board.objects.create(title='1글', user=user1)
board2 = Board.objects.create(title='2글', user=user1)
board3 = Board.objects.create(title='3글', user=user2)
c1 = Comment.objects.create(content='1글1댓글', user=user1, board=board1)
c2 = Comment.objects.create(content='1글2댓글', user=user2, board=board1)
c3 = Comment.objects.create(content='1글3댓글', user=user1, board=board1)
c4 = Comment.objects.create(content='1글4댓글', user=user2, board=board1)
c5 = Comment.objects.create(content='2글1댓글', user=user1, board=board2)
c6 = Comment.objects.create(content='!1글5댓글', user=user2, board=board1)
c7 = Comment.objects.create(content='!2글2댓글', user=user2, board=board2)
- $ python manage.py shell_plus
- 20190620 Shell 페이지 참조
- $ python manage.py startapp manytomany
- modelrelation-settings.py의 INSTALLED_APPS에 등록(manytomany)
manytomany - models.py 클래스 정의(Doctor, Patient, Reservation)

![2](.\images\2.png)

- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py shell_plus
- 20190620 Shell 페이지 참조
- manytomany - models.py 코드 추가
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    def __str__(self):
        return f'{self.id}번 환자 {self.name}'
- $ python manage.py makemigrations
- $ python manage.py migrate
- $ python manage.py shell_plus
- 20190620 Shell 페이지 참조
- manytomany - models.py 코드 추가
class Patient(models.Model):
    name = models.CharField(max_length=20)
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')

※ related_name='patients' 의 역할
- 역으로 호출할 때의 참조
- 상황에 따라 필수
- doctor.patient_set.all() -> doctor.patients.all()
- manytomany - models.py 코드 수정
Revervation(중개 모델) 주석 처리
Through 구문 삭제
오류 발생(ValueError: Cannot alter field manytomany)
-> migrations - __init__.py를 제외한 파일 전체 삭제 / db.sqlite3 삭제 후 다시 migrate