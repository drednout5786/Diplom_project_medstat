from django.contrib.auth import get_user_model, login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import HttpResponseRedirect
from django.http import Http404, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage, get_connection

from django.views.generic import UpdateView

from .forms import RegistrationUserForm
from .models import ArticlesUser
from .tokens import account_activation_token

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'

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

# https://stackoverflow.com/questions/55578387/email-verification-in-django
# https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
# https://stackoverflow.com/questions/47177696/noreversematch-with-keyword-argument-uidb64-with-django-2-0
def register(request):
    # User = get_user_model()
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if ArticlesUser.objects.filter(email__iexact=email).count() == 0:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('users/email_template.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                            'token': account_activation_token.make_token(user),
                        })
                print('message:', message)
                to_email = form.cleaned_data.get('email')
                # https://docs.djangoproject.com/en/2.0/topics/email/
                with get_connection() as connection:
                    EmailMessage(
                        subject=mail_subject, body=message, to=[to_email],
                        connection=connection,
                    ).send(fail_silently=False)
                # email = EmailMessage(subject=mail_subject, body=message, to=[to_email])
                # email.send(fail_silently=False)
                return render(request, 'users/acc_active_sent.html')
        else:
            return render(request, 'users/registration.html', {'form': form})
    else:
        form = RegistrationUserForm()
    return render(request, 'users/registration.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = ArticlesUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, ArticlesUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # messages.success(request, 'Profile updated successfully')
        return HttpResponseRedirect(reverse('users:success_verification'))
    else:
        # messages.error(request, 'Error updating your profile')
        return HttpResponse('Медстатистика: Activation link is invalid!')

# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
def success_verification(request):
    return render(request, 'users/success_verification.html')
