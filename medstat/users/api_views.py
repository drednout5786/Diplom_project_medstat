from .models import ArticlesUser, Infofile
from .serializer import ArticlesUserSerializer, InfofileSerializer
from articles.models import Tag, Article, SubscriberRequest
from articles.serializer import TagSerializer, ArticleSerializer, SubscriberRequestSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


class InfofileViewSet(viewsets.ModelViewSet):
    # queryset = Infofile.objects.all()
    queryset = Infofile.objects.prefetch_related('user')  # Оптимизация запросов
    serializer_class = InfofileSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]


# class ArticlesUserViewSet(viewsets.ModelViewSet):
#     queryset = ArticlesUser.objects.all()
#     serializer_class = ArticlesUserSerializer
