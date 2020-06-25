from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Tag, Subscriber_request
from .forms import ArticleForm
# from .forms import EmailForm
from .forms import RequestForm
from datetime import datetime
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.conf import settings
# User = settings.AUTH_USER_MODEL

# Create your views (представление) here.

def main_page(request):
    art_all = Article.objects.all().order_by('-article_date')
    return render(request, 'articles/category.html', {'articles': art_all})

@login_required
def article_description(request, id):
    art_one = get_object_or_404(Article, id=id)
    tags_article_all = Article.objects.get(id=id).article_tag.all()
    tags_all = Tag.objects.all()
    article_11 = get_object_or_404(Article, id=14)
    article_12 = get_object_or_404(Article, id=20)
    article_13 = get_object_or_404(Article, id=5)
    article_14 = get_object_or_404(Article, id=12)

    context = {
        'article': art_one,
        'tags_article_all': tags_article_all,
        'tags_all': tags_all,
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/single.html', context)

def tag_articles(request, id):
    tag_one = get_object_or_404(Tag, id=id)
    # получаем все статьи, которые имеют тэг tag_one
    articles_all = Article.objects.filter(article_tag__tag_name=tag_one)
    tags_all = Tag.objects.all()
    context = {
        'tag': tag_one,
        'articles_all': articles_all,
        'tags_all': tags_all,
    }
    return render(request, 'articles/tag_articles.html', context)

@user_passes_test(lambda user: user.is_superuser)
def article_add(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = ArticleForm()
        return render(request, 'articles/article_add.html', {'form': form})
    else:
        form = ArticleForm(request.POST, files=request.FILES) #  POST - После отправки данных из формы
        if form.is_valid():
            # обработка данных
            # Первый способ создания формы
            # name = form.cleaned_data['name']
            # text = form.cleaned_data['text']
            # tags = form.cleaned_data['tags']
            # print(f'{name}, {text}, {tags}')
            # article_object = Article(article_name=name, article_text=text, article_date=datetime.now(), article_img=ImageFile(open("media/articles/happy_lion.jpg", "rb")))
            # article_object.save()
            # Второй способ создания формы
            form.save()
            # Переход по адресу index
            return HttpResponseRedirect(reverse('articles:index'))
        else:
            return render(request, 'articles/article_add.html', {'form': form})

def service(request):
    article_11 = get_object_or_404(Article, id=14)
    article_12 = get_object_or_404(Article, id=20)
    article_13 = get_object_or_404(Article, id=5)
    article_14 = get_object_or_404(Article, id=12)
    context = {
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/service.html', context)

@login_required
def request_service(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = RequestForm()
        return render(request, 'articles/request_service.html', {'form': form})
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles:success_request'))
        else:
            return render(request, 'articles/request_service.html', {'form': form})

@login_required
def success_request(request):
        return render(request, 'articles/success_request.html')

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'tags'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'articles/article_update.html'
    success_url = reverse_lazy('articles:index')

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    model = Article
    success_url = reverse_lazy('articles:index')

class PermissionMixin:
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self): # перенаправляет пользователя на login_url
        return HttpResponseRedirect(reverse('users:login'))

class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'articles/tag_list.html'
    context_object_name = 'tags'

    #def get_queryset(self):
    # можно наложить условия на объекты
        #return Tag.objects.all()

class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'articles/tag_one.html'

class TagUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    fields = '__all__'
    template_name = 'articles/tag_update.html'
    success_url = reverse_lazy('articles:tag_list')

class TagCreateView(PermissionMixin, UserPassesTestMixin, CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'articles/tag_create.html'
    success_url = reverse_lazy('articles:tag_list')

class TagDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/tag_delete.html'
    model = Tag
    success_url = reverse_lazy('articles:tag_list')
