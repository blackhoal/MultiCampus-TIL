from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# @app.route('/send')
# def send():
#     return render_template('send.html')
#
# @app.route('/receive')
# def receive():
#     # user: 'jason', message: 'Long time no see'
#     user = request.args.get('user')
#     message = request.args.get('message')
#     return render_template('receive.html', user=user, message=message)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('lotto_round')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    # lotto = response.text # string
    lotto = response.json() # json
    # 방법 1
    # winner = []
    # for n in range(1, 7):
    #     winner.append(lotto[f'drwtNo{n}'])

    # 방법 2 - list comprehension
    a = [lotto[f'drwtNo{n}'] for n in range(1, 7)]
    b = lotto['bnusNo']
    winner = f'{a} + {b}'

    # my_numbers 가져오기
    my_numbers = [int(n) for n in request.args.get('my_numbers').split()]

    # 같은 숫자 갯수 확인 -> set을 사용
    matched = len(set(a) & set(my_numbers))

    # matched의 갯수에 따른 등수
    if matched == 6:
        result = '1등'
    elif matched == 5:
        if lotto['bnusNo'] in my_numbers:
            result = '2등'
        else:
            result = '3등'
    elif matched == 4:
        result = '4등'
    elif matched == 3:
        result = '5등'
    else:
        result = '꽝'

    return render_template('lotto_result.html', lotto=winner, lotto_round=lotto_round, my_numbers=my_numbers, result=result)

if __name__ == '__main__':
    app.run(debug=True)