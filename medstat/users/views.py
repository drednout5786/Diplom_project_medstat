from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationUserForm
from django.views.generic import CreateView, UpdateView
from .models import ArticlesUser


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLoginView_2(LoginView):
    template_name = 'users/success_registration.html'

class UserCreateView(CreateView):
    model = ArticlesUser
    template_name = 'users/registration.html'
    form_class = RegistrationUserForm
    success_url = reverse_lazy('users:success_register')


class SubscribeUpdateView(LoginRequiredMixin, UpdateView):
    model = ArticlesUser
    fields = ['is_subscribed']
    template_name = 'users/subscribe.html'
    success_url = reverse_lazy('users:success_subscribe')

# @login_required
# def subscribe(request):
#     if request.method == 'GET':  # Когда мы открываем шаблон
#         form = EmailForm()
#         return render(request, 'users/subscribe.html', {'form': form})
#     else:
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             # temp = form.save(commit=False)
#             # temp.subscribe_name = request.username
#             # temp.subscribe_email = request.email
#             # temp.save()
#             # обработка данных
#             # Первый способ создания формы
#             # name = form.cleaned_data['subscribe_name']
#             # email = form.cleaned_data['subscribe_email']
#             # print(f'{name}, {email}')
#             # subscriber_object = Subscriber(subscribe_name=name, subscribe_email=email, subscribe_date=datetime.now())
#             # subscriber_object.save()
#             # Второй способ создания формы
#             form.save()
#             return HttpResponseRedirect(reverse('users:success_subscribe'))
#         else:
#             return render(request, 'users/subscribe.html', {'form': form})
#
def success_subscribe(request):
        return render(request, 'users/success_subscribe.html')