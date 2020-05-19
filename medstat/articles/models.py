from django.db import models
from datetime import datetime
from django.db import models
from datetime import datetime
import os
from django.conf import settings

class Tag(models.Model):
    tag_name = models.CharField('название тэга', max_length=1000)

    def __str__(self):
        return f'{self.tag_name}'


class Article(models.Model):
    article_name = models.CharField('заголовок статьи', max_length=1000, null=True)
    article_text = models.CharField('текст статьи', max_length=10000, null=True)
    article_date = models.DateTimeField('дата публикации статьи', default=datetime.now())
    article_tag = models.ManyToManyField(Tag)
    article_img = models.ImageField('рисунок к статье', upload_to='articles', null=True, blank=True)

    def __str__(self):
        return f'{self.article_name}, опубликована: {self.article_date}'


class Subscriber(models.Model):
    subscribe_name = models.CharField('Ваше имя', max_length=100, null=True)
    subscribe_email = models.CharField('Ваш email', max_length=100)
    subscribe_date = models.DateTimeField('Дата подписки', default=datetime.now())

    def __str__(self):
        return f'{self.subscribe_name}, email: {self.subscribe_email}'

