import requests
import random
from flask import Flask,render_template, request
from decouple import config

app = Flask(__name__)

# Telegram
token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

# Naver
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
papago_url = 'https://openapi.naver.com/v1/papago/n2mt'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # request.args # GET
    # request.forms # POST
    # print(request.get_json())

    # 딕셔너리 가져오는 방식
    # 1. lotto['key'] -> key가 없을 시 에러 발생
    # 2. lotto.get('key') -> key가 없으면 None 반환
    message = request.get_json().get('message')
    print(message)

    # Data 가져오기
    if message is not None:
        chat_id = message.get('from').get('id')
        text = message.get('text')

        # 1. 로또
        if text == '/로또':
            text = random.sample(range(1, 46), 6)

        # 2. 네이버 번역
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
            }
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:]
            }
            papago_res = requests.post(papago_url, headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')

        # sendMessage 요청 보내기
        send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
        response = requests.get(send_url)

    return '', 200  # body, status_code

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    token = '843884211:AAG8EJkGVrFWASjFt5pajaHsd7JA_Z0LRF0'
    api_url = f'https://api.telegram.org/bot{token}'
    chat_id = '894319426'  # getUpdates - From - ID
    # text = input('메시지를 입력하세요:')
    # text = random.sample(range(1, 46), 6)
    text = request.args.get('message')

    response = requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '전송 완료'



if __name__ == '__main__':
    app.run(debug=True)