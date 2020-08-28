from django.test import TestCase
from articles.models import Article, Tag, Subscriber_request
from users.models import ArticlesUser

# https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing
# Самый простейший вариант тестирования. Без подключения дополнительных модулей и баз.
class ArticleTestCase_Easy(TestCase):
    # Тестирование поведения объектов модели Article (тестирование методов модели)
    def test_1_how_many_tags(self):

        tag1 = Tag.objects.create(tag_name='Методы')
        tag2 = Tag.objects.create(tag_name='Визуализация')
        tag3 = Tag.objects.create(tag_name='Анализ')
        article = Article.objects.create(article_name='text_name', article_text='test_text')
        article.article_tag.add(tag1, tag2, tag3)
        print('ТЕСТ 1')
        print('Тэги: ', tag1.tag_name, tag2.tag_name, tag3.tag_name)
        print('Название статьи: ', article.article_name, 'Текст статьи: ', article.article_text, '\n')

        self.assertEqual(article.tag_number(), 3)

    def test_2_is_one_tag(self):
        print('ТЕСТ 2')
        tag1 = Tag.objects.create(tag_name='Методы')
        tag2 = Tag.objects.create(tag_name='Визуализация')
        article = Article.objects.create(article_name='text_name', article_text='test_text')
        article.article_tag.add(tag1, tag2)

        print('Тэги: ', tag1.tag_name, tag2.tag_name)
        print('Название статьи: ', article.article_name, 'Текст статьи: ', article.article_text, '\n')

        self.assertFalse(article.is_tag_one())

    # Тестирование поведения объектов модели Tag (тестирование методов модели)
    def test_3_how_many_articles(self):
        print('ТЕСТ 3')
        tag = Tag.objects.create(tag_name='Методы')
        article1 = Article.objects.create(article_name='text_name1', article_text='test_text1')
        article1.article_tag.add(tag)
        article2 = Article.objects.create(article_name='text_name2', article_text='test_text2')
        article2.article_tag.add(tag)

        print('Тэги: ', tag.tag_name)
        print('Название статьи 1: ', article1.article_name, 'Текст статьи: ', article1.article_text)
        print('Название статьи 2: ', article2.article_name, 'Текст статьи: ', article2.article_text, '\n')

        self.assertEqual(tag.art_number(), 2)

    def test_4_is_art_not_none(self):
        print('ТЕСТ 4')
        tag = Tag.objects.create(tag_name='Методы')
        article1 = Article.objects.create(article_name='text_name1', article_text='test_text1')
        article1.article_tag.add(tag)
        article2 = Article.objects.create(article_name='text_name2', article_text='test_text2')
        article2.article_tag.add(tag)

        print('Тэги: ', tag.tag_name)
        print('Название статьи 1: ', article1.article_name, 'Текст статьи: ', article1.article_text)
        print('Название статьи 2: ', article2.article_name, 'Текст статьи: ', article2.article_text, '\n')

        self.assertTrue(tag.is_art_not_none())

    def test_5_subscribe_request(self):
        print('ТЕСТ 5')
        user = ArticlesUser.objects.create(email='user@user.ru')
        print('Пользователь: ', user)

        self.assertTrue(user.email_len_not_null())