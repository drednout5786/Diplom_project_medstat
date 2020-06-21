from django.db import models
from datetime import datetime
from django.db import models
from datetime import datetime
import os
from django.conf import settings
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

class Subscriber(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribe_name = models.CharField('Ваше имя', max_length=100, null=True)
    subscribe_email = models.CharField('Ваш email', max_length=100)
    subscribe_date = models.DateTimeField('Дата подписки', default=datetime.now())

    def __str__(self):
        return f'{self.subscribe_name}, email: {self.subscribe_email}'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Subscriber_request(models.Model):
    subscribe_request_name = models.CharField('Ваше имя', max_length=100)
    subscribe_request_email = models.CharField('Ваш email', max_length=100)
    subscribe_request_date = models.DateTimeField('Дата обращения', default=datetime.now())
    subscribe_request_text = models.TextField('Текст обращения', max_length=10000)

    def __str__(self):
        return f'{self.subscribe_request_name}, email: {self.subscribe_request_email}, обращение: {self.subscribe_request_text}'