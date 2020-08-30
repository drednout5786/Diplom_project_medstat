from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.db.models import signals
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.conf import settings

# Create your models here.

# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
# User модель и ее параметры https://djbook.ru/rel3.0/ref/contrib/auth.html#django.contrib.auth.models.User

# https://webdevblog.ru/sovremennyj-sposob-sozdanie-polzovatelskoj-modeli-user-v-django/
class ArticlesUser(AbstractUser):
    email = models.EmailField('E-mail', max_length=100, unique=True)
    is_subscribed = models.BooleanField('Подписка на новости сайта', default=True)

    def email_len_not_null(self):  # длина email не нулевая
        if len(self.email) > 0:
            return True
        return False

    def __str__(self):
        return f'{self.email}'
        # return f'{self.email}, длина email не нулевая: {self.email_len_not_null()}'

class Infofile(models.Model):
    date_visit = models.DateTimeField('Дата посещения сайта', default=datetime.now())
    user = models.ForeignKey(ArticlesUser, on_delete=models.CASCADE)

# Здесь мы определили функцию user_post_save и связали ее с сигналом post_save
# (который запускается после сохранения модели), отправленным моделью ArticlesUser
# ТЕСТИРОВАНИЕ возможности использования сигналов
@receiver(post_save, sender = ArticlesUser)
def create_info(sender, instance, **kwargs):
    Infofile.objects.create(user=instance, date_visit=datetime.now())


# Верификация email пользователя
# https://github.com/itsvinayak/user_login_and_register/blob/master/user/views.py
# https://github.com/rasca/django-verify-email/blob/master/verify_email/views.py
# https://stackoverflow.com/questions/55578387/email-verification-in-django

# https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
# Генерация токенов используя сигналы
# Если надо, чтобы у каждого пользователя был автоматически сгенерированный токен, можно поймать post_save сигнал пользователя.
@receiver(post_save, sender=ArticlesUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

