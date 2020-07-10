from django.test import TestCase
from mixer.backend.django import mixer
from articles.models import Article, Tag, Subscriber_request
from users.models import ArticlesUser

# Использование mixer pip install mixer
# Successfully installed mixer
# mixer http://klen.github.io/mixer.html

# 1 вариант Использования mixer
class ArticleTestCase_Mixer(TestCase):
    # Тестирование поведения объектов модели Article (тестирование методов модели)
    def setUp(self):
        self.tag1 = mixer.blend(Tag, tag_name=mixer.RANDOM)
        self.tag2 = mixer.blend(Tag, tag_name=mixer.RANDOM)

        self.article_1 = mixer.blend(Article, article_name=mixer.FAKE)
        self.article_1.article_tag.add(self.tag1, self.tag2)
        self.article_2 = mixer.blend(Article, article_name=mixer.FAKE)
        self.article_2.article_tag.add(self.tag1)

        self.user = mixer.blend(ArticlesUser, email=mixer.FAKE)

        # print('Тэги: ', self.tag1.tag_name, '\n', self.tag2.tag_name)
        # print('Название статьи: ', self.article_1.article_name, '\nТекст статьи: ', self.article_1.article_text, '\n')
        # print('Название статьи: ', self.article_2.article_name, '\nТекст статьи: ', self.article_2.article_text, '\n')
        # print('Пользователь: ', self.user)

    def test_16_how_many_tags(self):
        self.assertEqual(self.article_1.tag_number(), 2)
        self.assertEqual(self.article_2.tag_number(), 1)

    def test_17_is_one_tag(self):
        self.assertFalse(self.article_1.is_tag_one())
        self.assertTrue(self.article_2.is_tag_one())

    # Тестирование поведения объектов модели Tag (тестирование методов модели)
    def test_18_how_many_articles(self):
        self.assertEqual(self.tag1.art_number(), 2)
        self.assertEqual(self.tag2.art_number(), 1)

    def test_19_is_art_not_none(self):
        self.assertTrue(self.tag1.is_art_not_none())
        self.assertTrue(self.tag2.is_art_not_none())

    def test_20_subscribe_request(self):
        self.assertTrue(self.user.email_len_not_null())