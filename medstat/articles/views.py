from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Tag, Subscriber_request
from users.models import ArticlesUser
from .forms import ArticleForm
from .forms import RequestForm
from datetime import datetime
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from .decorators import counted
from django.http import Http404

# Create your views (представление) here.

@counted
def main_page(request):
    art_all = Article.active_objects.all().order_by('?')
    # art_all = Article.objects.filter(is_active=True)
    # art_all = Article.objects.all().order_by('?')  # Статьи вперемешку

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
    some_info_1 = 'удалить!!!'
    some_info_2 = 'тестирование шаблонных тэгов'
    return render(request, 'articles/category.html', {'articles': articles, 'info_1': some_info_1, 'info_2': some_info_2})


@login_required
@counted
def article_description(request, id):
    art_one = get_object_or_404(Article, id=id)
    # tags_article_all = Article.active_objects.get(id=id).article_tag.all()
    tags_article_all = Article.active_objects.get(id=id).article_tag.filter(is_active=True)
    tags_all = Tag.active_objects.all()
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

@counted
def tag_articles(request, id):
    tag_one = get_object_or_404(Tag, id=id)
    # получаем все статьи, которые имеют тэг tag_one
    # articles_all = Article.objects.filter(article_tag__tag_name=tag_one)
    articles_all = Article.active_objects.filter(article_tag=tag_one)
    tags_all = Tag.active_objects.all()
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

@counted
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
def success_request(request):
        return render(request, 'articles/success_request.html')

@login_required
def request_service(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = RequestForm()
        return render(request, 'articles/request_service.html', {'form': form})
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.subscribe_request_name = request.user
            temp.subscribe_request_type = 'SP'
            temp.save()
            # form.save()
            return HttpResponseRedirect(reverse('articles:success_request'))
        else:
            return render(request, 'articles/request_service.html', {'form': form})

@login_required
def request_consultation(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = RequestForm()
        return render(request, 'articles/request_consultation.html', {'form': form})
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.subscribe_request_name = request.user
            temp.subscribe_request_type = 'CO'
            temp.save()
            return HttpResponseRedirect(reverse('articles:success_request'))
        else:
            return render(request, 'articles/request_consultation.html', {'form': form})

@login_required
def request_review(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = RequestForm()
        return render(request, 'articles/request_review.html', {'form': form})
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.subscribe_request_name = request.user
            temp.subscribe_request_type = 'RV'
            temp.save()
            return HttpResponseRedirect(reverse('articles:success_request'))
        else:
            return render(request, 'articles/request_review.html', {'form': form})

@login_required
def request_question(request):
    if request.method == 'GET':  # Когда мы открываем шаблон
        form = RequestForm()
        return render(request, 'articles/request_question.html', {'form': form})
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.subscribe_request_name = request.user
            temp.subscribe_request_type = 'QS'
            temp.save()
            return HttpResponseRedirect(reverse('articles:success_request'))
        else:
            return render(request, 'articles/request_question.html', {'form': form})
#------------------------------------------------------
class PermissionMixin:
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self): # перенаправляет пользователя на login_url
        return HttpResponseRedirect(reverse('users:login'))

# Статьи ------------------------------------------------------
class ArticleListView(PermissionMixin, UserPassesTestMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'tags'

class ArticleUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'articles/article_update.html'
    success_url = reverse_lazy('articles:index')

class ArticleDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/article_delete.html'
    model = Article
    success_url = reverse_lazy('articles:index')

# Тэги ------------------------------------------------------
# class TagListView(LoginRequiredMixin, ListView): # Разрешает заходить авторизованному пользователю
class TagListView(PermissionMixin, UserPassesTestMixin, ListView):
    model = Tag
    template_name = 'articles/tag_list.html'
    context_object_name = 'tags'
    paginate_by = 10

    def get_queryset(self):  # наложить условия на объекты
    #     return Tag.objects.filter(is_active=True)
        return Tag.active_objects.filter()

class TagDetailView(PermissionMixin, UserPassesTestMixin, DetailView):
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

# Запросы ------------------------------------------------------
class ReqListView(PermissionMixin, UserPassesTestMixin, ListView):
    model = Subscriber_request
    template_name = 'articles/request_list.html'
    context_object_name = 'reqs'
    paginate_by = 10

    def get_queryset(self):
    # можно наложить условия на объекты
    #     return Tag.objects.filter(is_active=True)
        return Subscriber_request.active_objects.filter()

class ReqUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Subscriber_request
    fields = '__all__'
    template_name = 'articles/request_update.html'
    success_url = reverse_lazy('articles:request_list')

class ReqDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/request_delete.html'
    model = Subscriber_request
    success_url = reverse_lazy('articles:request_list')

# -------------------------------------------------------------------
class ReqListView_SP(PermissionMixin, UserPassesTestMixin, ListView):
    model = Subscriber_request
    template_name = 'articles/request_list_SP.html'
    context_object_name = 'reqs'
    paginate_by = 10
    def get_queryset(self):
        return Subscriber_request.active_objects.filter(subscribe_request_type='SP')

class ReqUpdateView_SP(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Subscriber_request
    fields = '__all__'
    template_name = 'articles/request_update.html'
    success_url = reverse_lazy('articles:request_list_SP')


class ReqDeleteView_SP(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/request_delete.html'
    model = Subscriber_request
    success_url = reverse_lazy('articles:request_list_SP')

# -------------------------------------------------------------------
class ReqListView_CO(PermissionMixin, UserPassesTestMixin, ListView):
    model = Subscriber_request
    template_name = 'articles/request_list_CO.html'
    context_object_name = 'reqs'
    paginate_by = 10

    def get_queryset(self):
        return Subscriber_request.active_objects.filter(subscribe_request_type='CO')

class ReqUpdateView_CO(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Subscriber_request
    fields = '__all__'
    template_name = 'articles/request_update.html'
    success_url = reverse_lazy('articles:request_list_CO')


class ReqDeleteView_CO(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/request_delete.html'
    model = Subscriber_request
    success_url = reverse_lazy('articles:request_list_CO')

# -------------------------------------------------------------------
class ReqListView_QS(PermissionMixin, UserPassesTestMixin, ListView):
    model = Subscriber_request
    template_name = 'articles/request_list_QS.html'
    context_object_name = 'reqs'
    paginate_by = 10

    def get_queryset(self):
        return Subscriber_request.active_objects.filter(subscribe_request_type='QS')


class ReqUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Subscriber_request
    fields = '__all__'
    template_name = 'articles/request_update.html'
    success_url = reverse_lazy('articles:request_list_QS')


class ReqDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/request_delete.html'
    model = Subscriber_request
    success_url = reverse_lazy('articles:request_list_QS')

# -------------------------------------------------------------------
#  Связываение запросов с моделью User: https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/
# -------------------------------------------------------------------
class ReqListView_RV(PermissionMixin, UserPassesTestMixin, ListView):
    model = Subscriber_request
    template_name = 'articles/request_list_RV.html'
    context_object_name = 'reqs'
    paginate_by = 10

    def get_queryset(self):
        return Subscriber_request.active_objects.filter(subscribe_request_type='RV')

class ReqUpdateView_RV(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Subscriber_request
    fields = '__all__'
    template_name = 'articles/request_update.html'
    success_url = reverse_lazy('articles:request_list_RV')

class ReqDeleteView_RV(PermissionMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/request_delete.html'
    model = Subscriber_request
    success_url = reverse_lazy('articles:request_list_RV')
# -------------------------------------------------------------------
#
# class ReqDetailView(PermissionMixin, UserPassesTestMixin, DetailView):
#     model = Subscriber_request
#     template_name = 'articles/request_one.html'



# Запрос по пользователям: https://ru.stackoverflow.com/questions/990082/Как-вывести-все-записи-пользователя-на-django

# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
def success_verification(request):
    return render(request, 'success_verification.html')

def verify(request, uuid):
    try:
        user = ArticlesUser.objects.get(verification_uuid=uuid, is_verified=False)
    except ArticlesUser.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()

    # return redirect('success_verification')
    return HttpResponseRedirect(reverse('articles:index'))