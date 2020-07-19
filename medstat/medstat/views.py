from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from articles.models import Article, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import random

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
    art_all = Article.active_objects.all()
    article_11 = get_object_or_404(Article, id=14)
    article_12 = get_object_or_404(Article, id=20)
    article_13 = get_object_or_404(Article, id=5)
    article_14 = get_object_or_404(Article, id=12)


    paginator = Paginator(art_all, 9) # Show 9 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    context = {
        'article_1': article_1,
        'article_2': article_2,
        'article': article_3,
        'article_4': article_4,
        'article_5': article_5,
        'articles': articles,
        'article_11': article_11,
        'article_12': article_12,
        'article_13': article_13,
        'article_14': article_14,
    }
    return render(request, 'articles/index.html', context)




