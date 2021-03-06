from django.db import models
from datetime import datetime
import os
from django.conf import settings
# from django.utils.functional import cached_property
from users.models import ArticlesUser  # импортируем из users

from django.core.signals import request_finished
from django.dispatch import receiver

#https://djbook.ru/rel1.9/topics/db/models.html#model-inheritance - наследование моделей

class AvtiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = AvtiveManager()
    is_active = models.BooleanField('Статус активности', default=True)
    class Meta:
        abstract = True  # Чтобы не было изменеий в таблицах

class Tag(IsActiveMixin, models.Model):
    tag_name = models.CharField('название тэга', max_length=1000, db_index=True)
    # db_index=True - введение индексации поля

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

    # cached_property предоставляет возможность кэшировать обращение к функции прямо в памяти процесса.
    # Такой вид кэша возможен только для методов не принимающих никаких параметров кроме self.
    # Такой кэш будет жить до тех пор пока существует соответствующий объект.
    # @cached_property
    def art_number(self):
        art = Article.objects.filter(article_tag__tag_name=self.tag_name)
        return len(art)

    # def is_art_not_none(self):  # Есть ли у тега статьи
    #     if len(Article.objects.filter(article_tag__tag_name=self.tag_name)) >= 1:
    #         return True
    #     return False

    def __str__(self):
        return f'{self.tag_name}'
        # return f'{self.tag_name} ({self.art_number()})'
        # return f'{self.tag_name}, количество статей по тэгу: {self.art_number()}'
        # return f'{self.tag_name}, количество статей по тэгу: {self.art_number()}, Есть ли у тега статьи: {self.is_art_not_none()}'

class Article(IsActiveMixin, models.Model):
    #, default = os.path.join(settings.MEDIA_ROOT,'articles','happy_lion.jpg')
    article_name = models.CharField('заголовок статьи', max_length=1000, null=True)
    article_text = models.TextField('текст статьи', max_length=10000, null=True)
    article_text_short = models.TextField('текст статьи 100 знаков', max_length=100, null=True)
    article_date = models.DateTimeField('дата публикации статьи', default=datetime.now())
    # article_rating = models.IntegerField(null = True)
    article_tag = models.ManyToManyField(Tag, verbose_name=("Тэг"))
    article_img = models.ImageField('рисунок к статье', upload_to='articles', null=True, blank=True)

    class Meta:
        ordering = ('-article_date',)
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    # @cached_property
    def get_all_tags(self):
        return Tag.active_objects.only('tag_name').all()
        # return Tag.active_objects.all()  # only('tag_name')

    # def tag_number(self):  # Количество тегов на статью
    #     return len(self.article_tag.all())
    #
    # def is_tag_one(self):  # Один ли тег у статьи
    #     if len(self.article_tag.all()) == 1:
    #         return True
    #     return False

    def __str__(self):
        return f'{self.article_name}'
        # return f'{self.article_name}, опубликована: {self.article_date}'
        # return f'{self.article_name}, опубликована: {self.article_date}, количество тэгов: {self.tag_number()}}'
        # return f'{self.article_name}, опубликована: {self.article_date}, количество тэгов: {self.tag_number()}, один ли тэг у статьи: {self.is_tag_one()}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}'
        # return f'{self.article_name}, опубликована: {self.article_date}, теги: {self.article_tag}, статья: {self.article_text}'
        # с перечислением тэгов
        # return "%s (%s)" % (self.article_name, ", ".join(Tag.tag_name for Tag in self.article_tag.all()))

#  https://stackoverflow.com/questions/26312219/operationalerror-no-such-column-django
class SubscriberRequest(IsActiveMixin, models.Model):
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
    subscribe_request_name = models.ForeignKey(ArticlesUser, on_delete=models.CASCADE, verbose_name=("Пользователь")) #связываем таблицы
    subscribe_request_type = models.CharField('Тип запроса', max_length=2, choices=REQUEST_TYPE_CHOICES, default=STATPROCESSING, blank=False)
    subscribe_request_subject = models.CharField('Тема обращения', max_length=200, blank=False, default='')
    subscribe_request_text = models.TextField('Текст обращения', max_length=10000, blank=False, default='')
    subscribe_request_date = models.DateTimeField('Дата обращения', default=datetime.now())
    subscribe_request_status = models.BooleanField('Статус выполнения', default=False)

    class Meta:
        ordering = ('-subscribe_request_date',)
        verbose_name = 'запрос на услугу'
        verbose_name_plural = 'запросы на услуги'

    def __str__(self):
        return f'{self.subscribe_request_name}, ' \
               f'тип запроса: {self.subscribe_request_type}, ' \
               f'статус запроса: {self.subscribe_request_status}, ' \
               f'дата обращения: {self.subscribe_request_date}, ' \
               f'тема обращения: {self.subscribe_request_subject}, ' \
               f'обращение: {self.subscribe_request_text}'

class PageHit(IsActiveMixin, models.Model):
    url = models.CharField(unique=True, max_length=2000)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'счётчик'
        verbose_name_plural = 'счётчики'

    def __str__(self):
        return f'{self.url}, количество просмотров: {self.count}'





