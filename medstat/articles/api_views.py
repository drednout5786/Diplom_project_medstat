from .models import Tag, Article, SubscriberRequest, PageHit
from users.models import ArticlesUser
from .serializer import TagSerializer, ArticleSerializer, SubscriberRequestSerializer, PageHitPopularSerializer  #, PageHitSerializer
from users.serializer import ArticlesUserSerializer, InfofileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthenticated_CUSTOM
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

# https://www.django-rest-framework.org/api-guide/permissions/

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAdminUser | ReadOnly]
    # permission_classes = [IsAuthenticated | ReadOnly]
    permission_classes = [IsAuthenticated_CUSTOM | ReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    # queryset = Article.objects.all()
    queryset = Article.objects.prefetch_related('article_tag')  # Оптимизация запросов: подгружаем то поле, которое будет часто использоваться.
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser | ReadOnly]


class SubscriberRequestViewSet(viewsets.ModelViewSet):
    queryset = SubscriberRequest.objects.all()
    serializer_class = SubscriberRequestSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]


# class PageHitViewSet(viewsets.ModelViewSet):
#     queryset = PageHit.objects.all()
#     serializer_class = PageHitSerializer


class PageHitPopularViewSet(viewsets.ModelViewSet):
    queryset = PageHit.objects.order_by('-count')
    # print('----------------------------------------queryset = ', queryset)
    serializer_class = PageHitPopularSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]