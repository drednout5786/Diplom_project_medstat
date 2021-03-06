# Generated by Django 3.0.7 on 2020-06-23 17:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.RemoveField(
            model_name='subscriber_request',
            name='subscribe_request_email',
        ),
        migrations.AddField(
            model_name='subscriber_request',
            name='subscribe_request_subject',
            field=models.CharField(default='', max_length=200, verbose_name='Тема обращения'),
        ),
        migrations.AddField(
            model_name='subscriber_request',
            name='subscribe_request_type',
            field=models.CharField(choices=[('SP', 'Статобработка'), ('CO', 'Консультация'), ('QS', 'Вопрос'), ('RV', 'Рецензия')], default='SP', max_length=2, verbose_name='Тип запроса'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 20, 27, 15, 821289), verbose_name='дата публикации статьи'),
        ),
        migrations.AlterField(
            model_name='subscriber_request',
            name='subscribe_request_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 20, 27, 15, 832644), verbose_name='Дата обращения'),
        ),
        migrations.AlterField(
            model_name='subscriber_request',
            name='subscribe_request_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscriber_request',
            name='subscribe_request_text',
            field=models.TextField(default='', max_length=10000, verbose_name='Текст обращения'),
        ),
    ]
