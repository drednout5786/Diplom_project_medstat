from .models import Tag, Article, SubscriberRequest, PageHit
from users.models import ArticlesUser
from .serializer import TagSerializer, ArticleSerializer, SubscriberRequestSerializer, PageHitPopularSerializer  #, PageHitSerializer
from users.serializer import ArticlesUserSerializer, InfofileSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SubscriberRequestViewSet(viewsets.ModelViewSet):
    queryset = SubscriberRequest.objects.all()
    serializer_class = SubscriberRequestSerializer
    permission_classes = [IsAdminUser]

# class PageHitViewSet(viewsets.ModelViewSet):
#     queryset = PageHit.objects.all()
#     serializer_class = PageHitSerializer


class PageHitPopularViewSet(viewsets.ModelViewSet):
    queryset = PageHit.objects.order_by('-count')
    # print('----------------------------------------queryset = ', queryset)
    serializer_class = PageHitPopularSerializer
    permission_classes = [IsAdminUser]