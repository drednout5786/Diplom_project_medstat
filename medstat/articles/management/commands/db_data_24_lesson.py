from django.core.management.base import BaseCommand
from articles.models import Article, Tag, Subscriber_request, PageHit
from users.models import ArticlesUser
from datetime import date, datetime
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Запрос в базу список тэгов с количеством статей + есть ли у тега статьи
        tags = Tag.objects.all()
        print(f'Всего тэгов: {len(tags)}')
        for i in range(len(tags)):
            print(f'{i}: {tags[i]}')

        # Запрос в базу список статей с количеством тэгов + 1 ли тэг у статьи
        articles = Article.objects.all()
        print(f'Всего статей: {len(articles)}')
        for i in range(len(articles)):
            print(f'{i}: {articles[i]}')

        # Запрос в базу список запросов + общее количество запросов
        requests = Subscriber_request.objects.all()
        print(f'Всего запросов всех видов: {len(requests)}')
        for i in range(len(requests)):
            print(f'{i}: {requests[i]}')

        # Запрос в базу список пользователей + длина email не нулевая + количество запросов от Пользователя
        art_users = ArticlesUser.objects.all()
        print(f'Всего зарегистрированных пользователей: {len(art_users)}')
        for i in range(len(art_users)):
            num = Subscriber_request.objects.filter(subscribe_request_name=art_users[i])
            # num = Subscriber_request.objects.filter(subscribe_request_name__email=art_users[i])
            print(f'{i}: {art_users[i]}, количество запросов: {len(num)}')