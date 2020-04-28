from django.core.management.base import BaseCommand
from articles.models import Article, Tag
from datetime import date, datetime
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **options):

        print('DB commands') # https://metanit.com/python/django/5.3.php
# Получение из бд

        # получить все имеющиеся объекты
        # articles = Article.objects.all()
        # print(articles)

        # articles = Article.objects.all()[5:10]
        # print(articles)

        # получить все имеющиеся объекты, если их больше 20
        articles = Article.objects.all()
        print(f'Всего статей: {len(articles)}')
        for i in range(len(articles)):
            print(f'{i}: {articles[i]}')

        # tags = Tag.objects.all()
        # print(tags)

# получить все объекты по определенному критерию
        # filter
        # tags = Tag.objects.filter(tag_name='математики улыбаются')
        # print(tags)

        # сложные filter начинается с, больше/меньше  https://docs.djangoproject.com/en/3.0/topics/db/queries/
        # art_1 = Article.objects.filter(article_name__startswith="Математики улыбаются")
        # art_2 = art_1.exclude(article_date__gte=timezone.now())
        # art_2 = art_1.filter(article_date__lte=timezone.now())
        # for i in range(len(art_2)):
        #     print(f'{i}: {art_2[i]}')

        # сложные filter содержит и не содержит
        # art_1 = Article.objects.filter(article_name__icontains="меди").exclude(article_name__icontains="медиа")
        # print(art_1)

        # OR
        # art_1 = Article.objects.exclude(article_name__icontains="меди").exclude(article_name__icontains="медиа")
        # print(len(art_1), art_1)

        # AND
        # art_1 = Article.objects.exclude(article_name__icontains="меди", article_text__icontains="медиа")
        # print(len(art_1), art_1)

        # order_by() '-' это indicates descending order
        # articles = Article.objects.filter(article_date__year=2020).order_by('article_date', '-article_name')
        # for i in range(len(articles)):
        #     print(f'{i}: {articles[i]}')

        # random To order randomly https://docs.djangoproject.com/en/3.0/ref/models/querysets/#queryset-api
        # Article.objects.order_by('?')

        # get - возвращает один объект по критерию
        # art_ = Article.objects.get(article_name='Covid-19. Статистика распространения')
        # print(art_)

        # исключить из выборки записи по критерию
        # tags = Tag.objects.exclude(tag_name='математики улыбаются')
        # print(tags)

        # возвращает словарь
        # все
        # articles = Article.objects.in_bulk()
        # for id in articles:
        #     print(articles[id].article_name)
        #     print(articles[id].article_date)

        # articles = Article.objects.in_bulk()
        # print(articles)
        # for id in articles:
        #     print(articles[id].article_name)
        #     print(articles[id].article_date)
        #     print(articles[id].article_tag)

        # выборочно по id
        # articles = Article.objects.in_bulk([1,3,4])
        # for id in articles:
        #     print(articles[id].article_name)
        #     print(articles[id].article_date)

# Связанные поля # https://metanit.com/python/django/5.7.php
        # art_ = Article.objects.get(article_name='Covid-19. Статистика распространения')
        # print(art_.article_tag.all())
        # print(art_.article_tag.first())

        # получим все тэги для одной статьи
        # tags_ = Article.objects.get(article_name="Стандартное отклонение и стандартная ошибка: разберем путаницу").article_tag.all()
        # print(tags_)

        # получаем все статьи, которые имеют тэг визуализация
        # art_ = Article.objects.filter(article_tag__tag_name="визуализация")
        # print(art_)

        # art_ = Article.objects.filter(article_tag__tag_name="новый тэг_1")
        # print(art_)

# Добавление в базу данных
        # create Создаем новый тэг
        # Tag.objects.create(tag_name='новый тэг_1')
        # tags = Tag.objects.all()
        # print(tags)

        # ИЛИ
        # t = Tag(tag_name='новый тэг_1')
        # t.save()
        # print(t.id)
        # tags = Tag.objects.all()
        # print(tags)
        #
        #
        # создадим новую статью с новым тэгом
        # a = Article.objects.create(article_name='Новый заголовок', article_text='Текст новой статьи',
        #                            article_date=timezone.now())
        # a.article_tag.add(t)
        # articles = Article.objects.all()
        # print(f'Всего статей: {len(articles)}')
        # for i in range(len(articles)):
        #     print(f'{i}: {articles[i]}')

        # НЕ РАБОТАЕТ со старым тэгом
        # a = Article.objects.create(article_name='Новый заголовок', article_text='Текст новой статьи',
        #                            article_date=timezone.now())
        # a.article_tag.add(3)
        # print(Article.objects.all())

        # POST https://stackoverflow.com/questions/51011540/django-throws-direct-assignment-to-the-forward-side-of-a-many-to-many-set-is-pr

        # art_1 = Article.objects.create(article_name="Новая статья_1")
        # # создадим новый тэг и добавим его в список тэгов новой статьи
        # art_1.article_tag.create(tag_name="новый тэг_1")
        # tags = Tag.objects.all()
        # print(tags)
        # articles = Article.objects.all()
        # print(articles)

        # save
        # new_tag = Tag(tag_name='Новый тег')
        # new_tag.save()
        # tags = Tag.objects.all()
        # print(tags)

# Метод get_or_create() возвращает объект, а если его нет в бд, то добавляет в бд новый объект
        # tag_, created = Tag.objects.get_or_create(tag_name="визуализация")
        # print(tag_.tag_name)
        # if created == True:
        #     print('Добавление произошло успешно.')
        # else:
        #     print('Данная запись уже есть в базе.')
        # tags = Tag.objects.all()
        # print(tags)

        # tag_, created = Tag.objects.get_or_create(tag_name="Новый тег")
        # print(tag_.tag_name)
        # if created == True:
        #     print('Добавление произошло успешно.')
        # else:
        #     print('Данная запись уже есть в базе.')
        # tags = Tag.objects.all()
        # print(tags)

# update

        # Tag.objects.filter(id=11).update(tag_name="математики улыбаются") # Другой тэг
        # tags = Tag.objects.all()
        # print(tags)

# Удаление

        # tag = Tag.objects.filter(tag_name='Новый тег')
        # tag = Tag.objects.filter(tag_name='новый тэг_1')
        # tag.delete()
        # tags = Tag.objects.all()
        # print(tags)

        # a = Article.objects.filter(article_name='Новая статья_1')
        # a.delete()
        # articles = Article.objects.exclude(article_name='Новый заголовок')
        # print(f'Всего статей: {len(articles)}')
        # for i in range(len(articles)):
        #     print(f'{i}: {articles[i]}')

        # tag_, created = Tag.objects.get_or_create(tag_name="Новый тег")
        # print(tag_.tag_name)
        # if created == True:
        #     print('Добавление произошло успешно.')
        # else:
        #     print('Данная запись уже есть в базе.')
        # tags = Tag.objects.all()
        # print(tags)
        #
        # Article.article_tag.add(tag_)





