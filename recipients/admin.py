from django.contrib import admin

from recipients.models import Recipients


@admin.register(Recipients)
class RecipientsAdmin(admin.ModelAdmin):
    """
    Регистрация класса "Recipients" из recipients/models.py в админ панели
    """
    list_display = ('email', 'name', 'description')
    search_fields = ('email', 'name', )
    list_filter = ('email', 'name',)
