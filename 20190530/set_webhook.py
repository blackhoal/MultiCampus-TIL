import requests
from decouple import config

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
flask_url = f'blackhoal.pythonanywhere.com/{token}'
set_url = f'{api_url}/setWebhook?url={flask_url}'

response = requests.get(set_url)
print(response.text)