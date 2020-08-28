from django.test import TestCase
from faker import Faker
from articles.models import Article, Tag, Subscriber_request
from users.models import ArticlesUser

# Использование Faker pip install faker
# Successfully installed faker-4.1.1
# faker https://faker.readthedocs.io/en/latest/index.html

class ArticleTestCase_Faker(TestCase):
    # Тестирование поведения объектов модели Article (тестирование методов модели)
    def setUp(self):
        data_generator = Faker(['ru_Ru'])

        self.tag1 = Tag.objects.create(tag_name=data_generator.name())
        self.tag2 = Tag.objects.create(tag_name=data_generator.name())

        self.article_1 = Article.objects.create(article_name=data_generator.name(), article_text=data_generator.text())
        self.article_1.article_tag.add(self.tag1, self.tag2)
        self.article_2 = Article.objects.create(article_name=data_generator.name(), article_text=data_generator.text())
        self.article_2.article_tag.add(self.tag1)

        self.user = ArticlesUser.objects.create(email=data_generator.email())

        # print('Тэги: ', self.tag1.tag_name, '\n', self.tag2.tag_name)
        # print('Название статьи: ', self.article_1.article_name, '\nТекст статьи: ', self.article_1.article_text, '\n')
        # print('Название статьи: ', self.article_2.article_name, '\nТекст статьи: ', self.article_2.article_text, '\n')
        # print('Пользователь: ', self.user)

    def test_6_how_many_tags(self):
        self.assertEqual(self.article_1.tag_number(), 2)
        self.assertEqual(self.article_2.tag_number(), 1)

    def test_7_is_one_tag(self):
        self.assertFalse(self.article_1.is_tag_one())
        self.assertTrue(self.article_2.is_tag_one())

    # Тестирование поведения объектов модели Tag (тестирование методов модели)
    def test_8_how_many_articles(self):
        self.assertEqual(self.tag1.art_number(), 2)
        self.assertEqual(self.tag2.art_number(), 1)

    def test_9_is_art_not_none(self):
        self.assertTrue(self.tag1.is_art_not_none())
        self.assertTrue(self.tag2.is_art_not_none())

    def test_10_subscribe_request(self):
        self.assertTrue(self.user.email_len_not_null())