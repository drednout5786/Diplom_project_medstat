from django.db import models
from datetime import datetime
from django.db import models
from datetime import datetime
import os
from django.conf import settings
from users.models import ArticlesUser #импортируем из users
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class Tag(models.Model):
    tag_name = models.CharField('название тэга', max_length=1000)

    def __str__(self):
        return f'{self.tag_name}'

class Article(models.Model):
    #, default = os.path.join(settings.MEDIA_ROOT,'articles','happy_lion.jpg')
    article_name = models.CharField('заголовок статьи', max_length=1000, null=True)
    article_text = models.CharField('текст статьи', max_length=10000, null=True)
    article_text_short = models.CharField('текст статьи 100 знаков', max_length=100, null=True)
    article_date = models.DateTimeField('дата публикации статьи', default=datetime.now())
    # article_rating = models.IntegerField(null = True)
    article_tag = models.ManyToManyField(Tag)
    article_img = models.ImageField('рисунок к статье', upload_to='articles', null=True, blank=True)

    def __str__(self):
        # return f'{self.article_name}'
        return f'{self.article_name}, опубликована: {self.article_date}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}, статья: {self.article_text}'
        # с перечислением тэгов
        # return "%s (%s)" % (self.article_name, ", ".join(Tag.tag_name for Tag in self.article_tag.all()))

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

#  https://stackoverflow.com/questions/26312219/operationalerror-no-such-column-django
class Subscriber_request(models.Model):
    STATPROCESSING = 'SP'
    CONSULTATION = 'CO'
    QUESTION = 'QS'
    REVIEW = 'RV'
    REQUEST_TYPE_CHOICES = [
        (STATPROCESSING, 'Статобработка'),
        (CONSULTATION, 'Консультация'),
        (QUESTION, 'Вопрос'),
        (REVIEW, 'Рецензия'),
    ]
    subscribe_request_name = models.ForeignKey(ArticlesUser, on_delete=models.CASCADE) #связываем таблицы
    subscribe_request_type = models.CharField('Тип запроса', max_length=2, choices=REQUEST_TYPE_CHOICES, default=STATPROCESSING, blank=False)
    subscribe_request_subject = models.CharField('Тема обращения', max_length=200, blank=False, default='')
    subscribe_request_text = models.TextField('Текст обращения', max_length=10000, blank=False, default='')
    subscribe_request_date = models.DateTimeField('Дата обращения', default=datetime.now())

    def __str__(self):
        return f'{self.subscribe_request_name}, тип запроса: {self.subscribe_request_type}, ' \
               f'дата обращения: {self.subscribe_request_date}, тема обращения: {self.subscribe_request_subject}, ' \
               f'обращение: {self.subscribe_request_text}'