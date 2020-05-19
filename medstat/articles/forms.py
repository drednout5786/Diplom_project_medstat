from django import forms
from .models import Tag
from .models import Article
from .models import Subscriber

class ArticleForm(forms.ModelForm):
    article_tag = forms.ModelMultipleChoiceField(label='Тэги', queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Article
        fields = '__all__'

class EmailForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('subscribe_name', 'subscribe_email')


