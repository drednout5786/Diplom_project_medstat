from django import forms
from .models import Tag
from .models import Article
from .models import SubscriberRequest

class ArticleForm(forms.ModelForm):
    article_tag = forms.ModelMultipleChoiceField(label='Тэги', queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Article  # Привязываем форму с конкретной моделью.
        fields = '__all__'  # Все поля отображать
        # fields = ('article_name', 'article_text') # Какие поля отображать
        # exclude = ('tags')  # Какие поля исключить.

class RequestForm(forms.ModelForm):
    class Meta:
        model = SubscriberRequest  # Привязываем форму с конкретной моделью.
        # fields = '__all__'
        fields = ('subscribe_request_subject', 'subscribe_request_text')


# class ArticleForm(forms.Form):
#     name = forms.CharField(label='Название статьи', max_length=1000)
#     text = forms.CharField(label='Текст статьи')
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())
# class EmailForm(forms.Form):
#     subscribe_name = forms.CharField(label='Введите Ваше имя', max_length=100)
#     subscribe_email = forms.CharField(label='Введите Ваш email', max_length=100)
# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber  # Привязываем форму с конкретной моделью.
#         fields = ('subscribe_name', 'subscribe_email')
