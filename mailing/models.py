from django.db import models

from recipients.models import Recipients

NULLABLE = {'blank': True, 'null': True}

FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [("Create", 'Создана'), ("Started", 'Отправлено'), ("Done", 'Завершена'), ]
LOGS_STATUS_CHOICES = [('success', 'успешно'), ('fail', 'неуспешно'),]


class MailingMessage(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingSettings(models.Model):
    first_datetime = models.DateTimeField(verbose_name='начало рассылки', auto_now_add=True)
    next_datetime = models.DateTimeField(verbose_name='next_datetime', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='конец рассылки', **NULLABLE)
    sending_period = models.CharField(max_length=50, verbose_name='период рассылки', choices=FREQUENCY_CHOICES)
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='сообщения')
    recipients = models.ManyToManyField(Recipients, verbose_name='получатели')
    settings_status = models.CharField(max_length=50, verbose_name='статус рассылки', choices=STATUS_OF_NEWSLETTER,
                                       default='Create')

    def __str__(self):
        return f'{self.message} отправляется каждый {self.sending_period} с {self.first_datetime}'

    class Meta:
        verbose_name = 'Настройка отправки'
        verbose_name_plural = 'Настройки отправки'


class MailingStatus(models.Model):
    last_datetime = models.DateTimeField(auto_now_add=True, verbose_name='последняя дата отправки')
    status = models.CharField(max_length=50, choices=LOGS_STATUS_CHOICES, default='', verbose_name='статус попытки')
    mailing_response = models.TextField(verbose_name='ответ сервера')
    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    recipient = models.ForeignKey(Recipients, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.status} отправлялось {self.last_datetime}, ответ сервера: {self.mailing_response}'

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = 'Статусы отправки'
