from django.test import TestCase
from mixer.backend.django import mixer
import pandas as pd
from articles.models import Article, Tag

# Использование generatedata
# generatedata https://www.generatedata.com/

class ArticleTestCase_csv(TestCase):
    # Тестирование поведения объектов модели Article (тестирование методов модели)
    def setUp(self):
        df_articles = pd.read_csv('data_test_articles.csv', sep=';')
        for _ , row in df_articles.iterrows():
            Article.objects.create(article_name=row['article_name'], article_text=row['article_text'])
        self.articles = Article.objects.all()
        # print('Статьи', len(self.articles), self.articles[0])

        df_tags = pd.read_csv('data_test_tags.csv', sep=';')
        for _ , row in df_tags.iterrows():
            Tag.objects.create(tag_name=row['tag_name'])
        self.tags = Tag.objects.all()
        # print('Тэги', len(self.tags), self.tags[0])

        self.article_1 = mixer.blend(Article, article_name=self.articles[0])
        self.article_1.article_tag.add(self.tags[1], self.tags[2])
        self.article_2 = mixer.blend(Article, article_name=self.articles[0])
        self.article_2.article_tag.add(self.tags[1])

        # print('Тэги: ', self.tags[1].tag_name, '\n', self.tags[2].tag_name)
        # print('Название статьи: ', self.article_1.article_name, '\nТекст статьи: ', self.article_1.article_text, '\n')
        # print('Название статьи: ', self.article_2.article_name, '\nТекст статьи: ', self.article_2.article_text, '\n')

    def test_21_how_many_tags(self):
        self.assertEqual(self.article_1.tag_number(), 2)
        self.assertEqual(self.article_2.tag_number(), 1)

    def test_22_is_one_tag(self):
        self.assertFalse(self.article_1.is_tag_one())
        self.assertTrue(self.article_2.is_tag_one())

    # Тестирование поведения объектов модели Tag (тестирование методов модели)
    def test_23_how_many_articles(self):
        self.assertEqual(self.tags[1].art_number(), 2)
        self.assertEqual(self.tags[2].art_number(), 1)

    def test_24_is_art_not_none(self):
        self.assertTrue(self.tags[1].is_art_not_none())
        self.assertTrue(self.tags[2].is_art_not_none())
