from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import ArticlesUser, Infofile
from django.db.models import signals
from django.core.mail import send_mail
from .forms import CustomUserChangeForm, RegistrationUserForm

# Register your models here.

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

def set_disactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

class ArticlesUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_subscribed', 'is_active', 'date_joined', 'last_login']
    actions = [set_active, set_disactive]
    ordering = ['date_joined', 'last_login']
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')

class InfofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_visit']
    ordering = ['date_visit']
    list_filter = ('user', 'date_visit')


admin.site.register(ArticlesUser, ArticlesUserAdmin)
admin.site.register(Infofile, InfofileAdmin)

# admin.site.register(ArticlesUser)

