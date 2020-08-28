from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer
from articles.models import Article, Tag
from users.models import ArticlesUser

class ViewsTest(TestCase):

    def setUp(self):
        # self.client = Client()  # Поднимаем сервер
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')  # Поднимаем сервер и тестируем определенный браузер

        ArticlesUser.objects.create_superuser(username='test_user', email='test@test.ru', password='123456')
        # ArticlesUser.objects.create_user(username='test_user', email='test@test.ru', password='123456')

        # Tag.objects.create(tag_name='test')

        self.tag = mixer.cycle(2).blend(Tag, tag_name=mixer.RANDOM)
        self.article_1 = mixer.blend(Article, article_name=mixer.FAKE)
        self.article_1.article_tag.add(self.tag[0], self.tag[1])
        self.article_2 = mixer.blend(Article, article_name=mixer.FAKE)
        self.article_2.article_tag.add(self.tag[0])
        # print('self.tag: ', self.tag)
        # print('self.article_1: ', self.article_1)
        # print('self.article_2: ', self.article_2)

        self.article = mixer.cycle(5).blend(Article)  # Генерация 5 статей
        # print('self.article: ', self.article)
        # print('Количество сгенерированных статей: ', len(self.article))

        # Пример с генератором
        gen_art_name = (v for v in ['art_name_1', 'art_name_2', 'art_name_3', 'art_name_4', 'art_name_5'])
        self.arts = mixer.cycle(5).blend(Article, article_name=gen_art_name)
        # print('self.arts: ', self.arts)
        # print('Количество сгенерированных статей: ', len(self.arts))


    # проверка статуса ответа по запросу
    # def test_status_main_page(self):
    #     response = self.client.get('/')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 200)

    # проверка статуса ответа по get запросу
    def test_1_status_request_service(self):
        response = self.client.get('/articles/request-service/')
        self.assertEqual(response.status_code, 302)  # 302 - код редиректа. Т.к. только авторизованные пользователи могут попасть на эту страницу.

    def test_2_status_articles_add(self):
        response = self.client.get('/articles/add/')
        self.assertEqual(response.status_code, 302)

    # тестирование доступа без авторизованного пользователя
    def test_3_status_create_tag(self):
        response = self.client.get('/articles/tag-one/1/')
        self.assertEqual(response.status_code, 302)

    # тестирование доступа с авторизованным пользователем
    def test_4_status_detail_tag(self):
        self.client.login(username='test_user', password='123456')  # Логинем пользователя
        response = self.client.get('/articles/tag-one/1/')
        self.assertEqual(response.status_code, 200)  # Для Суперюзера
        # self.assertEqual(response.status_code, 302)  # Для зарегистрированного пользователя

    # тестирование post запроса
    def test_5_status_post_tag(self):
        self.client.login(username='test_user', password='123456')
        response = self.client.post('/articles/tag-create/', {'tag_name': 'test_tag'})
        self.assertEqual(response.status_code, 302)

    # def test_6_status_post_add_tag(self):
    #     self.client.login(username='test_user', password='123456')
    #     response = self.client.post('/articles/article_add/', {'article_name': 'Название статьи',
    #                                                            'article_text': 'Текст статьи',
    #                                                            'article_text_short': 'Текст статьи короткий'})
    #     self.assertEqual(response.status_code, 200)

    def test_7_details(self):
        self.client.login(username='test_user', password='123456')  # Логинем пользователя
        response = self.client.get('/articles/tag-one/2/')
        # print('ОТВЕТ:', response.context)
        self.assertEqual(len(response.context), 2)