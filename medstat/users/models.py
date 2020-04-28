from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class ArticlesUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    def __str__(self):
        return f'{self.email}, {self.username}, {self.first_name}, {self.last_name}, {self.is_staff}, {self.is_active},' \
               f' {self.is_superuser}, {self.date_joined}, {self.password}'

class Service(models.Model):
    service_type = ['Заказать статобработку', 'Рецензия статистика']
    subject = models.CharField('тема обращения', max_length=100, null=True)
    desctiption = models.CharField('текст обращения', max_length=5000, null=True)
    date_ctration = models.DateTimeField('дата обращения', default=datetime.now())
    email = models.ForeignKey(ArticlesUser, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.service_type}, {self.subject},{self.desctiption},{self.date_ctration},{self.email}'
