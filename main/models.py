
from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}

ACTIVE_CHOICES = [
    (True, 'Активна'),
    (False, 'Неактивна'),
]

LOG_CHOICES = [
    (True, 'Успешно'),
    (False, 'Неудача'),
]
# Create your models here.


class Client(models.Model):

    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(unique=True, verbose_name='Почта')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Отправитель')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиентов'
        permissions = [
            ('client_delete', 'Может удалять клиентов')
        ]


class Message(models.Model):

    subject = models.CharField(max_length=250, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Содержание')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец сообщения')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class Mailing(models.Model):

    stat_mailing = [('Запущена', 'Запущена'),
                    ('Завершена', 'Завершена'),
                    ('Создана', 'Создана')]
    period_mailing = [('Раз в день', 'Раз в день'),
                      ('Раз в неделю', 'Раз в неделю'),
                      ('Раз в месяц', 'Раз в месяц')]
    name = models.CharField(max_length=50, verbose_name='Рассылка', **NULLABLE)
    periodicity = models.CharField(choices=period_mailing, default='Один раз в день', verbose_name='Периодичность')
    state = models.CharField(max_length=20, choices=stat_mailing, default='Запущена', verbose_name='Статус')
    client = models.ManyToManyField(Client, verbose_name='клиент')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='Начало рассылки')
    next_date = models.DateTimeField(default=timezone.now, verbose_name='Следующая рассылка')
    end_date = models.DateTimeField(verbose_name='Конец рассылки', **NULLABLE)

    is_activated = models.BooleanField(default=True, choices=ACTIVE_CHOICES, verbose_name='Активность')


    def __str__(self):
        return f'{self.name} {self.state} {self.periodicity}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_date',)
        permissions = [
            ('set_is_activated', 'Может отключать рассылку'),
            ('can_view', 'Может просматривать рассылки')
        ]


class Logs(models.Model):

    stat_mailing = [('start', 'Запущена'),
                    ('finish', 'Завершена')]
    data = models.DateTimeField(verbose_name='Дата', **NULLABLE)
    state = models.CharField(default=False, max_length=10, choices=LOG_CHOICES, verbose_name='Попытка', **NULLABLE)
    email_answer = models.BooleanField(default=False, verbose_name='Ответ от почты')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)
    last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='Время рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.last_mailing_time} - {self.state}'

    class Meta:
        verbose_name = 'Лог сообщения'
        verbose_name_plural = 'Логов сообщений'




