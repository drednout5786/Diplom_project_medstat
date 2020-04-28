from django.db import models
from datetime import datetime
import os
from django.conf import settings

class Tag(models.Model):
    tag_name = models.CharField('название тэга', max_length=100)

    def __str__(self):
        return f'{self.tag_name}'


class Article(models.Model):
    article_name = models.CharField('заголовок статьи', max_length=1000, null=True)
    article_text = models.CharField('текст статьи', max_length=10000, null=True)
    article_date = models.DateTimeField('дата публикации статьи', default=datetime.now())
    article_tag = models.ManyToManyField(Tag)
    article_img = models.ImageField('рисунок к статье', upload_to='articles', null=True, blank=True)
    #, default = os.path.join(settings.MEDIA_ROOT,'articles','happy_lion.jpg')

    def __str__(self):
        # return f'{self.article_name}'
        # return f'{self.article_name}, опубликована: {self.article_date}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}, статья: {self.article_text}'
        # с перечислением тэгов
        return "%s (%s)" % (self.article_name, ", ".join(Tag.tag_name for Tag in self.article_tag.all()))

