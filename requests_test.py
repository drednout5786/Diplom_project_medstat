# Запрос к API через консоль
import requests
import os

SERVER ='http://127.0.0.1:8000/'
PAGE = 'api/v0/tag/'
tag = '2'

response = requests.get(os.path.join(SERVER, PAGE, tag))

print(response.status_code, response.text)

# Запрос к API через утилиту curl
# https://proft.me/2013/08/17/spravochnik-po-komandam-wget-i-curl/
# curl -X GET http://127.0.0.1:8000/api/v0/tag/2/
# Работает, если тэги на английском языке. На русском выдает абракадабру.

# Запрос к API через Postman
# https://www.postman.com/downloads/
# Делаю GET запрос: http://127.0.0.1:8000/api/v0/
# Post тоже можно делать.

