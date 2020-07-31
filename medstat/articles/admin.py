from django.contrib import admin
from .models import Tag, Article, SubscriberRequest, PageHit



def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


def set_disactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_name', 'article_text', 'is_active', 'article_date']
    actions = [set_active, set_disactive]
    ordering = ['article_date']
    list_filter = ('article_name', 'article_text', 'is_active', 'article_date')
    search_fields = ('article_name', 'article_text')  # https://pocoz.gitbooks.io/django-v-primerah/nastrojka-sposoba-otobrazheniya-modelej.html


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name', 'is_active']
    actions = [set_active, set_disactive]
    search_fields = ('tag_name',)


class SubscriberRequestAdmin(admin.ModelAdmin):
    list_display = ['subscribe_request_name', 'subscribe_request_type', 'subscribe_request_subject',
                    'subscribe_request_text', 'subscribe_request_date', 'is_active']
    actions = [set_active, set_disactive]
    search_fields = ('subscribe_request_subject', 'subscribe_request_text')


class PageHitAdmin(admin.ModelAdmin):
    list_display = ['url', 'count', 'is_active']
    actions = [set_active, set_disactive]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SubscriberRequest, SubscriberRequestAdmin)
admin.site.register(PageHit, PageHitAdmin)

# admin.site.register(Tag)
# admin.site.register(Article)
# admin.site.register(Subscriber_request)

