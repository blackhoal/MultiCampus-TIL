from django.shortcuts import render
from datetime import datetime
import random
import json
import requests

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def adios(request):
    return render(request, 'pages/adios.html')

def dinner(request):
    menu = ['닭가슴살', '프로틴', '두부', '목살 구이']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'pages/introduce.html', context)

def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num1':num1, 'num2': num2, 'num3': num3}
    return render(request, 'pages/times.html', context)

def circle(request, r):
    area = 3.14 * (r ** 2)
    context = {'r': r, 'area': area}
    return render(request, 'pages/circle.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '깐풍기']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = ['jason', 'Andrew']
    datetimenow = datetime.now()
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow
    }
    return render(request, 'pages/template_language.html', context)

def birthday(request):
    today = datetime.now()
    if today.month == 12 and today.day == 4:
        result = True
    else:
        result = False
    context = {
        'result': result
    }
    return render(request, 'pages/birthday.html', context)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    context = {'message1': message1,
               'message2': message2}
    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def get(request):
    lottos = range(1, 46)
    pick = random.sample(lottos, 6)
    name = request.GET.get('name')
    context = {
        'pick': pick,
        'name': name
    }
    return render(request, 'pages/get.html', context)

# lotto / get
# get -> 1~45의 수 중 6개를 뽑아 리스트로 만들어 넘긴다.
# get -> 사용자로부터 이름을 입력받아 넘긴다.

def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('name')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text)

    winner = []
    for i in range(1, 7):
        # 2차 강사님 코드
        winner.append(lotto[f'drwtNo{i}'])
        # 1차 강사님 코드
        # a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]

    picked = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(picked))
    # 교집합

    if matched == 6:
        result = '안녕히 계세요 여러분 전 이 세상의 모든 굴레와 속박을 벗어던지고 제 행복을 찾아 떠납니다 여러분도 행복하세요'
    elif matched == 5:
        result = '3등'
    elif matched == 4:
        result = '4등'
    elif matched == 3:
        result = '5등'
    else:
        result = '꽝'

    context = {
        'name': name,
        'result': result
    }
    return render(request, 'pages/picklotto.html', context)

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    # 1. form 태그로 발생한 데이터 수신
    word = request.GET.get('word')

    # 2. artii API를 통해 보낸 응답 결과를 text 형태로 font에 저장
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    # 3. fonts(str)를 font 리스트의 형태로 저장
    fonts = fonts.split('\n')

    # 4. fonts(list) 안에 들어있는 요소 중 하나를 선택하여 font에 저장
    font = random.choice(fonts)

    # 5. 4에서 사용자로부터 받은 word와 랜덤하게 뽑은 font를 가지고 다시 요청
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result': result
    }
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd
    }
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')