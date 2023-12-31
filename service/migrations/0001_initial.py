# Generated by Django 4.2.4 on 2023-08-24 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('surname', models.CharField(max_length=150, verbose_name='отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'ordering': ('first_name', 'last_name', 'surname'),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=150, verbose_name='тема сообщения')),
                ('body', models.TextField()),
                ('mailing_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время рассылки')),
                ('periodicity', models.PositiveSmallIntegerField(choices=[(1, 'Раз в день'), (2, 'Раз в неделю'), (3, 'Раз в месяц')], default=1, verbose_name='периодичность')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Создана'), (2, 'Запущена'), (3, 'Завершена')], default=1, verbose_name='статус рассылки')),
                ('clients', models.ManyToManyField(to='service.client', verbose_name='клиенты')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attempt', models.DateTimeField(verbose_name='Дата попытки')),
                ('status', models.CharField(max_length=150, verbose_name='Статус попытки')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ сервера')),
                ('mailing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.client', verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
