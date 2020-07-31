from django.conf.urls import url, include
from .models import ArticlesUser, Infofile
from django.contrib.auth.models import AbstractUser
from rest_framework import routers, serializers, viewsets


# https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/viewsets
# Документация на русском
class ArticlesUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticlesUser
        exclude = ['email']
        # fields = '__all__'

class InfofileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Infofile
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'infofile-detail'},
        }
