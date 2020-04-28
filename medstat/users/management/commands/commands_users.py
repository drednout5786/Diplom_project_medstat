from django.core.management.base import BaseCommand
from users.models import ArticlesUser, Service

class Command(BaseCommand):

    def handle(self, *args, **options):

        print('DB commands')

        # https: // qarus.ru / 21703843 - django - abstractusers - create_user - ne - rabotaet - dolzhnym - obrazom /

        # Создание пользователей без проверки на уникальность
        # user = ArticlesUser.objects.create_user(username='User_1', email='mail_1@mail.ru', password='654321')
        # user = ArticlesUser.objects.create_user(username='User_2', email='mail_2@mail.ru', password='654987')
        # user.save()

        # Создание пользователей с проверкой на уникальность username и email
        # https://djbook.ru/rel1.8/topics/auth/customizing.html

        # username = 'User_5'
        # email = 'mail_4@mail.ru'
        # password = '321654'
        # try:
        #     user = ArticlesUser.objects.get(email=email)
        #     if user:
        #         print('Пользователь с данным email уже существует.')
        #         # message = 'User with the following email id already exists'
        #         # return render(request, 'signup.html', {'message': message})
        #     else:
        #         user = ArticlesUser.objects.create_user(username=username, email=email, password=password)
        #         user.save()
        #         # login(request, user)
        # except ArticlesUser.DoesNotExist:
        #     print('Пользователь с данным username уже существует.')

        # получить все имеющиеся объекты, если их больше 20
        users = ArticlesUser.objects.all()
        print(f'Всего полльзователей: {len(users)}')
        for i in range(len(users)):
            print(f'{i}: {users[i]}')

        # sevices = Service.objects.all()
        # print(f'Всего заказов на услуги: {len(sevices)}')
        # for i in range(len(sevices)):
        #     print(f'{i}: {sevices[i]}')





#P.S. urls, views и т.д.
# https://docs.djangoproject.com/en/3.0/intro/overview/
# https://metanit.com/python/django/2.1.php
# https://djbook.ru/rel1.7/topics/db/models.html
# https://qna.habr.com/q/264387 формы для пароля