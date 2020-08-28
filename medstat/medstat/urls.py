"""medstat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # подключаем файл настроек
from django.conf.urls.static import static  # прописываем ссылки на статик файлы
from django.conf.urls import url
from medstat import views
from rest_framework import routers
from articles.api_views import TagViewSet, ArticleViewSet, SubscriberRequestViewSet, PageHitPopularViewSet  #, PageHitViewSet
from users.api_views import InfofileViewSet  #, ArticlesUserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('article', ArticleViewSet)
router.register('request', SubscriberRequestViewSet)
# router.register('pagehit', PageHitViewSet)
router.register('pagehit_popular', PageHitPopularViewSet)
# router.register('articles_user', ArticlesUserViewSet)
router.register('infofile', InfofileViewSet)

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')),
    # path('api-tag/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls)),
]

if settings.DEBUG is True:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

