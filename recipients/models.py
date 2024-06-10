from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Recipients(models.Model):
    """
    Модель клиентов, которым будет направлена рассылка
    """
    email = models.EmailField(verbose_name='Почта', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Сообщение')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Менеджер рассылок', **NULLABLE)

    def __str__(self):
        return f'{self.email} - {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
