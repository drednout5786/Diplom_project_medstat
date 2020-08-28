from django.conf.urls import url, include
from .models import Tag, Article, SubscriberRequest, PageHit
from users.models import ArticlesUser
from rest_framework import routers, serializers, viewsets


# https://www.django-rest-framework.org/#installation

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# У одной модели может быть несколько сериалайзеров
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    article_tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'article-detail', 'lookup_field': 'pk'},
        }

class SubscriberRequestSerializer(serializers.HyperlinkedModelSerializer):
    # email = serializers.StringRelatedField(many=False)
    class Meta:
        model = SubscriberRequest
        exclude = ['subscribe_request_name']
        # fields = '__all__'
        # extra_kwargs = {
        #     'url': {'view_name': 'subscriberrequest-detail', 'lookup_field': 'pk'},
        # }

# class PageHitSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PageHit
#         fields = '__all__'

class PageHitPopularSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageHit
        fields = '__all__'