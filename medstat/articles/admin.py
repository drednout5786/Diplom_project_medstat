from django.contrib import admin

# Register your models here.

from .models import Tag, Article, Subscriber, Subscriber_request

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Subscriber)
admin.site.register(Subscriber_request)

