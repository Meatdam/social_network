from django.contrib import admin

from mailing.models import MailingSettings, MailingMessage, MailingStatus


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    """
    Регистрация класса "MailingSettings" из mailing/models.py в админ панели
    """
    list_display = ('first_datetime', 'end_time', 'sending_period', 'message', 'settings_status')


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    """
    Регистрация класса "MailingMessage" из mailing/models.py в админ панели
    """
    list_display = ('title', 'content')
    search_fields = ('title', 'content', )
    list_filter = ('title', 'content',)


@admin.register(MailingStatus)
class MailingStatusAdmin(admin.ModelAdmin):
    """
    Регистрация класса "MailingStatus" из mailing/models.py в админ панели
    """
    list_display = ('last_datetime','status','mailing_response','mailing_list','recipient')
    search_fields = ('last_datetime','status','mailing_response','mailing_list','recipient')
    list_filter = ('last_datetime','status','mailing_response','mailing_list','recipient')

