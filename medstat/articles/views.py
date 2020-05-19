from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Article, Tag, Subscriber
from .forms import ArticleForm
from .forms import EmailForm
from datetime import datetime
from django.core.files.images import ImageFile

# Create your views (представление) here.

def main_page(request):
    art_all = Article.objects.all()
    return render(request, 'articles/category.html', {'articles': art_all})

def article_description(request, id):
    art_one = get_object_or_404(Article, id=id)
    tags_all = Article.objects.get(id=id).article_tag.all()
    article_11 = get_object_or_404(Article, id=6)
    article_12 = get_object_or_404(Article, id=10)
    article_13 = get_object_or_404(Article, id=9)
    article_14 = get_object_or_404(Article, id=12)

    context = {
        'article': art_one,
        'tags': tags_all,
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/single.html', context)

def article_add(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = ArticleForm()
        return render(request, 'articles/article_add.html', {'form': form})
    else:
        form = ArticleForm(request.POST, files=request.FILES) #  POST - После отправки данных из формы
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles:index'))
        else:
            return render(request, 'articles/article_add.html', {'form': form})

def subscribe(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = EmailForm()
        return render(request, 'articles/subscribe.html', {'form': form})
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
              form.save()
              return HttpResponseRedirect(reverse('articles:index'))
        else:
            return render(request, 'articles/subscribe.html', {'form': form})

def service(request):
    article_11 = get_object_or_404(Article, id=6)
    article_12 = get_object_or_404(Article, id=10)
    article_13 = get_object_or_404(Article, id=9)
    article_14 = get_object_or_404(Article, id=12)
    context = {
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/service.html', context)
