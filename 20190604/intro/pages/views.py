from django.shortcuts import render
from datetime import datetime
import random
import json
import requests

def index(request):
    return render(request, 'pages/index.html')

def hola(request):
    return render(request, 'pages/hola.html')

def dinner(request):
    menu = ['닭가슴살', '우유', '고구마', '방울토마토']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/introduce.html', context)

# 1. variable routing을 통해 숫자를 2개 받아 곱셈 결과를 출력

def times(request, a, b):
    x = a*b
    context = {'a':a, 'b':b, 'x':x}
    return render(request, 'pages/times.html', context)

# 2. 반지름(r)을 인자로 받아 원의 넓이를 구하시오

def circle(request, r):
    s = 3.141592*r**2
    context = {'r':r, 's':s}
    return render(request, 'pages/circle.html', context)

def template_language(request):
    menus = ['짜장면','탕수육','짬뽕','양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple','banana','cucumber','mango']
    empty_list = ['juan','justin','nwith']
    datetimenow = datetime.now()
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':messages,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
    }
    return render(request, 'pages/template_language.html', context)

def birthday(request):
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    context = {'result': result}
    return render(request, 'pages/birthday.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message': message, 'message2': message2}
    return render(request, 'pages/catch.html', context)

# Lotto / get
# get -> 1~45의 수 중에서 6개를 뽑아 리스트로 만들어 넘긴다.
# get -> 사용자로부터 이름을 입력받아 넘긴다.

def Lotto(request):
    return render(request, 'pages/lotto.html')

def get(request):
    lotto = sorted(random.sample(range(1, 46), 6))
    name = request.GET.get('name')
    context = {'lotto':lotto, 'name':name}
    return render(request, 'pages/get.html', context)

def Lotto2(request):
    return render(request, 'pages/lotto2.html')

def winnum(request):
    name = request.GET.get('name')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text)

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    pick = sorted(random.sample(range(1, 46), 6))
    match = len(set(winner)&set(pick))

    if match == 6:
        result = '1등입니다. 퇴사!'
    elif match == 5:
        result = '3등입니다. 휴가 ㄱㄱ'
    elif match == 4:
        result = '4등입니다. 술 ㄱㄱ'
    elif match == 3:
        result = '5등입니다. 로또 ㄱㄱ'
    else:
        result = '꽝'

    context = {'name':name, 'result':result}

    return render(request, 'pages/winnum.html', context)

def art(request):
    return render(request, 'pages/art.html')

def masterpiece(request):
    #1. form 태그로 날린 데이터를 받는다.
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 font 리스트의 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font에 저장.
    font = random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 랜덤하게 뽑은 font를 가지고 다시 요청을 보냄.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'result': result}
    return render(request, 'pages/masterpiece.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name':name, 'pwd':pwd}
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')

