from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from articles.models import Article, Tag
import random

# Create your views (представление) here.

# https://pastebin.com/fAU6qmgA
def home_page(request):
    # random_idx = random.randint(1, Article.objects.count())
    # art_random = get_object_or_404(Article, id=random_idx)

    article_1 = get_object_or_404(Article, id=15)
    article_2 = get_object_or_404(Article, id=3)
    article_3 = get_object_or_404(Article, id=11)
    article_4 = get_object_or_404(Article, id=8)
    article_5 = get_object_or_404(Article, id=20)
    article_all = Article.objects.all().order_by('?')
    article_11 = get_object_or_404(Article, id=14)
    article_12 = get_object_or_404(Article, id=20)
    article_13 = get_object_or_404(Article, id=5)
    article_14 = get_object_or_404(Article, id=12)

    context = {
        'article_1': article_1,
        'article_2': article_2,
        'article': article_3,
        'article_4': article_4,
        'article_5': article_5,
        'article_all': article_all,
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/index.html', context)




