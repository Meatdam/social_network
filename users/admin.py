from django.contrib import admin

from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Регистрация класса "User" из users/models.py в админ панель
    """
    list_display = ('id', 'username', 'email')
