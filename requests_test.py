# Запрос к API через консоль
import requests
import os

# SERVER ='http://127.0.0.1:8000/'
# PAGE = 'api/v0/tag/'
# tag = '2'
#
# response = requests.get(os.path.join(SERVER, PAGE, tag))
#
# print(response.status_code, response.text)

# Запрос к API через утилиту curl
# https://proft.me/2013/08/17/spravochnik-po-komandam-wget-i-curl/
# curl -X GET http://127.0.0.1:8000/api/v0/tag/2/
# Работает, если тэги на английском языке. На русском выдает абракадабру.

# Запрос к API через Postman
# https://www.postman.com/downloads/
# Делаю GET запрос: http://127.0.0.1:8000/api/v0/
# Post тоже можно делать.

#-----------------------------------------------------------------------------------
# Урок 29
# https://www.django-rest-framework.org/api-guide/authentication/#api-reference
# 401 - нет прав на это действие
# 204 - все хорошо, но я вам ничего не вернул

TAG = "http://127.0.0.1:8000/api/v0/tag/16/"
# response = requests.get(TAG)
# response = requests.delete(TAG)
# print(response.status_code, response.text)
# 403 {"detail":"Authentication credentials were not provided."}

# БАЗОВАЯ АВТОРИЗАЦИЯ
# https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication
# auth = ('zzzxxx', 'zxc123asd456')
# response = requests.get(TAG)
# 200 {"url":"http://127.0.0.1:8000/api/v0/tag/17/","is_active":true,"tag_name":"тестовый тэг3"}
# response = requests.delete(TAG, auth=auth)
# 204
# print(response.status_code, response.text)

# Авторизация по токену
# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
# python manage.py drf_create_token admin
# Generated token 2d7010e7c4ba0cb8c033a62d83cc888145efcc05 for user admin
# curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'

token = '9bea529a698320f0659540930509c4b2aa2609dd'

headers = {'Authorization': f'Token {token}'}
# response = requests.get(TAG, headers=headers)
# 200 {"url":"http://127.0.0.1:8000/api/v0/tag/16/","is_active":true,"tag_name":"тестовый тэг1"}

# response = requests.delete(TAG)
# 403 {"detail":"Authentication credentials were not provided."}

response = requests.delete(TAG, headers=headers)
# 204
print(response.status_code, response.text)




