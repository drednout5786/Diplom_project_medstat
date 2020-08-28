from django.test import TestCase
from faker import Faker #   installed faker-4.1.1
from .models import Article, Tag, Subscriber_request
from users.models import ArticlesUser  # импортируем из users
from mixer.backend.django import mixer
import pandas as pd

# faker https://faker.readthedocs.io/en/latest/index.html
# mixer http://klen.github.io/mixer.html
# generatedata https://www.generatedata.com/

# Тесты с урока

# Использование generatedata
# class ArticleTestCase_csv(TestCase):
#
#     def setUp(self):
#         data = pd.read_csv('data_test.csv', sep=';')
#         for _ , row in data.iterrows():
#             Article.objects.create(article_name=row['article_name'], article_text=row['article_text'])
#
#         tag1 = mixer.blend(Tag, tag_name=mixer.RANDOM)
#         tag2 = mixer.blend(Tag, tag_name=mixer.RANDOM)
#         self.article = mixer.blend(Article, article_name=mixer.FAKE)
#         self.article.article_tag.add(tag1, tag2)
#
#     def test_how_many_tags(self):
#         articles = Article.objects.all()
#         print(len(articles))
#
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one_tag(self):
#         self.assertFalse(self.article.is_tag_one())

# 1 вариант Использования mixer pip install mixer
# class ArticleTestCase_mixer(TestCase):
#
#     def setUp(self):
#         tag1 = mixer.blend(Tag)
#         tag2 = mixer.blend(Tag)
#         self.article = mixer.blend(Article)
#         self.article.article_tag.add(tag1, tag2)
#
#         print(tag1.tag_name, tag2.tag_name)
#         print(self.article.article_name, self.article.article_text)
#
#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())

# 2 вариант Использования mixer pip install mixer
# class ArticleTestCase_mixer(TestCase):
#
#     def setUp(self):
#         tag1 = mixer.blend(Tag, tag_name='Методы')
#         tag2 = mixer.blend(Tag, tag_name=mixer.RANDOM)
#         self.article = mixer.blend(Article, article_name=mixer.FAKE)
#         self.article.article_tag.add(tag1, tag2)
#
#         print(tag1.tag_name, tag2.tag_name)
#         print(self.article.article_name, self.article.article_text)
#
#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())

# Использование Faker pip install faker
# class ArticleTestCase(TestCase):
#
#     def setUp(self):
#         data_generator = Faker(['ru_Ru'])
#         tag1 = Tag.objects.create(tag_name=data_generator.name())
#         tag2 = Tag.objects.create(tag_name=data_generator.name())
#         self.article = Article.objects.create(article_name=data_generator.name(), article_text=data_generator.text())
#         self.article.article_tag.add(tag1, tag2)
#
#         print(tag1.tag_name, tag2.tag_name)
#         print(self.article.article_name, self.article.article_text)
#
#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())

# class ArticleTestCase(TestCase):
#
#     def setUp(self):
#         data_generator = Faker(['ru_Ru'])
#         tag1 = Tag.objects.create(tag_name='Методы')
#         tag2 = Tag.objects.create(tag_name='Визуализация')
#         self.article = Article.objects.create(article_name='text_name', article_text='test_text')
#         self.article.article_tag.add(tag1, tag2)
#
#         print(tag1.tag_name, tag2.tag_name)
#         print(self.article.article_name, self.article.article_text)
#
# def tearDown(self):  # https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing
#     # Очистка после каждого метода
#     pass

#     def test_how_many(self):
#         self.assertEqual(self.article.tag_number(), 2)
#
#     def test_is_one(self):
#         self.assertFalse(self.article.is_tag_one())

