from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import ArticlesUser

from .forms import CustomUserChangeForm, RegistrationUserForm

# Register your models here.
admin.site.register(ArticlesUser)

# https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
# admin.site.register(UserAdmin)
# class CustomUserAdmin(UserAdmin):
#     add_form = RegistrationUserForm
#     form = CustomUserChangeForm
#     model = ArticlesUser
#     list_display = ('email', 'is_staff', 'is_subscribed',)
#     list_filter = ('email', 'is_staff', 'is_subscribed',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_subscribed')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#
# admin.site.register(ArticlesUser, CustomUserAdmin)