# Generated by Django 3.0.5 on 2020-04-28 18:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, null=True, verbose_name='тема обращения статьи')),
                ('desctiption', models.CharField(max_length=5000, null=True, verbose_name='текст обращения')),
                ('date_ctration', models.DateTimeField(default=datetime.datetime(2020, 4, 28, 21, 49, 47, 791849), verbose_name='дата обращения')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]