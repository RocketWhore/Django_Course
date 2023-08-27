from django.db import models
# from django.forms import ModelForm
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    surname = models.CharField(max_length=150, verbose_name='отчество')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)

    def str(self) -> str:
        return f'{self.last_name} {self.first_name} {self.surname}, email: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = "клиенты"
        ordering = ('first_name', 'last_name', 'surname')


class Message(models.Model):
    TITLE_CHOICES_PERIODICITY = [
        (1, 'Раз в день'),
        (2, 'Раз в неделю',),
        (3, 'Раз в месяц',),
    ]

    TITLE_CHOICES_STATUS = [
        (1, 'Создана'),
        (2, 'Запущена',),
        (3, 'Завершена',),
    ]
    theme = models.CharField(max_length=150, verbose_name='тема сообщения')
    body = models.TextField()
    mailing_time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now, verbose_name='время  начала рассылки')
    periodicity = models.PositiveSmallIntegerField(verbose_name="периодичность", choices=TITLE_CHOICES_PERIODICITY,
                                                   default=1)
    status = models.PositiveSmallIntegerField(verbose_name='статус рассылки', choices=TITLE_CHOICES_STATUS, default=1)
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.theme} {self.status}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = 'Сообщения'


class Log(models.Model):
    date_attempt = models.DateTimeField(verbose_name='Дата попытки')
    status = models.CharField(max_length=150, verbose_name='Статус попытки')
    answer = models.TextField(**NULLABLE, verbose_name='ответ сервера')
    mailing = models.ForeignKey(Message, **NULLABLE, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, verbose_name='пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.status} {self.date_attempt}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
