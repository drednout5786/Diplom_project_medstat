from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from articles.models import Article, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import random

# Create your views (представление) here.

# https://pastebin.com/fAU6qmgA
def home_page(request):
    art_all = Article.active_objects.defer('article_text').all()
    # art_all = Article.active_objects.prefetch_related('article_tag').all()
    # prefetch_related делает 7 запросов. Мой вариант делает 5 запросов.

    paginator = Paginator(art_all, 9)  # Show 9 articles per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    art_list = [15, 3, 11, 8, 13, 14, 20, 5, 12]
    art_context = []
    for art_i in art_list:
        for art_ in art_all:
            if art_.id == art_i:
                art_context.append(art_)
                break

    context = {
        'articles': articles,
        'article_1': art_context[0],
        'article_2': art_context[1],
        'article_3': art_context[2],
        'article_4': art_context[3],
        'article_5': art_context[4],
        'article_11': art_context[5],
        'article_12': art_context[6],
        'article_13': art_context[7],
        'article_14': art_context[8],
    }
    return render(request, 'articles/index.html', context)




