from .models import ArticlesUser, Infofile
from .serializer import ArticlesUserSerializer, InfofileSerializer
from articles.models import Tag, Article, SubscriberRequest
from articles.serializer import TagSerializer, ArticleSerializer, SubscriberRequestSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


# class ArticlesUserViewSet(viewsets.ModelViewSet):
#     queryset = ArticlesUser.objects.all()
#     serializer_class = ArticlesUserSerializer

class InfofileViewSet(viewsets.ModelViewSet):
    queryset = Infofile.objects.all()
    serializer_class = InfofileSerializer
    permission_classes = [IsAdminUser]