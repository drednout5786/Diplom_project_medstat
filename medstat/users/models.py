from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# https://webdevblog.ru/sovremennyj-sposob-sozdanie-polzovatelskoj-modeli-user-v-django/
class ArticlesUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    is_subscribed = models.BooleanField('Подписка на новости сайта', default=True)

    def __str__(self):
        return f'{self.email}'