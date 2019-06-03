from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def adios(request):
    return render(request, 'adios.html')

def dinner(request):
    menu = ['닭가슴살', '프로틴', '두부', '목살 구이']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name': name, 'age': age}
    return render(request, 'introduce.html', context)

def times(request, num1, num2):
    num3 = num1 * num2
    context = {'num1':num1, 'num2': num2, 'num3': num3}
    return render(request, 'times.html', context)

def circle(request, r):
    area = 3.14 * (r ** 2)
    context = {'r': r, 'area': area}
    return render(request, 'circle.html', context)

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
    return render(request, 'template_language.html', context)

def birthday(request):
    today = datetime.now()
    if today.month == 12 and today.day == 4:
        result = True
    else:
        result = False
    context = {
        'result': result
    }
    return render(request, 'birthday.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    context = {'message1': message1,
               'message2': message2}
    return render(request, 'catch.html', context)

def lottoinput(request):
    return render(request, 'lottoinput.html')

def lottooutput(request):
    name = request.GET.get('name')
    number = request.GET.get('number')
    context = {'name': name,
               'number': number}
    return render(request, 'lottooutput.html', context)


# lotto / get
# get -> 1~45의 수 중 6개를 뽑아 리스트로 만들어 넘긴다.
# get -> 사용자로부터 이름을 입력받아 넘긴다.
