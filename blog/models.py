from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    """
    Модель блога, в котором будут храниться статьи
    """
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='blog', **NULLABLE, verbose_name='Изображение')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE, verbose_name='Админ блога', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
