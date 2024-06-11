from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Регистрация класса "Blog" из blog/models.py в админ панели
    """
    list_display = ('title', 'content', 'image', 'created_at', 'owner', 'is_published')
    list_filter = ('title', 'owner', 'is_published')
