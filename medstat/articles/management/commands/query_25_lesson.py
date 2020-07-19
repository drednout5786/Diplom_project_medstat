#  Не простейшие запросы
# https://docs.djangoproject.com/en/3.0/ref/models/querysets/ - документация с примерами

from django.core.management.base import BaseCommand
from articles.models import Article, Tag, Subscriber_request
from users.models import ArticlesUser
from datetime import datetime, date
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):

        # больше/меньше
        # articles = Article.objects.filter(article_date__year__gt=2019)
        # articles = Article.objects.filter(article_date__year__lt=2021)

        # articles = Article.objects.exclude(article_date__lt=datetime(2020, 6, 30, 17, 5))
        # articles = Article.objects.exclude(article_date__gt=datetime(2020, 6, 30, 17, 5))

        art_ = Article.objects.filter(article_name__contains="Математики улыбаются")
        articles = art_.filter(article_date__lte=timezone.now())

        # запросы с условиями на текстовые данные

        # articles = Article.objects.filter(article_name__startswith='Б')
        # articles = Article.objects.exclude(article_name__startswith='Б')

        # OR
        # articles = Article.objects.filter(article_name__icontains="меди").filter(article_name__icontains="мед")

        # AND
        # articles = Article.objects.filter(article_name__icontains="меди", article_text__icontains="медиана")


        # Запросы к связанным моделям

        # articles = Article.objects.filter(article_tag__tag_name__startswith='м')

        # получаем все статьи, которые имеют тэг рецензия статистика
        # articles = Article.objects.filter(article_tag__tag_name="рецензия статистика")

        for i in range(len(articles)):
            print(f'{i}: {articles[i]}')

        # получим все тэги для одной статьи
        # tags_ = Article.objects.get(article_name="Стандартное отклонение и стандартная ошибка: разберем путаницу").article_tag.all()
        #
        # for i in range(len(tags_)):
        #     print(f'{i}: {tags_[i]}')
