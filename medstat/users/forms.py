from django import forms
from .models import ArticlesUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.admin import UserAdmin

class RegistrationUserForm(UserCreationForm):
    class Meta:
        model = ArticlesUser
        # fields = '__all__'
        fields = ('username', 'email', 'is_subscribed')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = ArticlesUser
        fields = ('is_subscribed',)

# class MyUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields': ('is_subscribed',)}),
#     )

# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber  # Привязываем форму с конкретной моделью.
#         fields = ('subscribe_name', 'subscribe_email')