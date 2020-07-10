from django.db import models
from django.contrib.auth.models import AbstractUser
# from articles.models import Subscriber_request

# Create your models here.

# https://webdevblog.ru/sovremennyj-sposob-sozdanie-polzovatelskoj-modeli-user-v-django/
class ArticlesUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    is_subscribed = models.BooleanField('Подписка на новости сайта', default=True)

    def email_len_not_null(self):  # длина email не нулевая
        # req = ArticlesUser.objects.filter(email=self.email)
        # req = Subscriber_request.objects.filter(subscribe_request_name=self.email)
        # print(len(req))
        # return len(req)
        if len(self.email) > 0:
            return True
        return False

    # def req_number(self):  # количество запросов
    #     # req = ArticlesUser.objects.filter(email=self.email)
    #     req = Subscriber_request.objects.filter(subscribe_request_name=self.email)
    #     print(len(req))
    #     return len(req)

    def __str__(self):
        # return f'{self.email}'
        return f'{self.email}, длина email не нулевая: {self.email_len_not_null()}'