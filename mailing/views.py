from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.views import TitleMixin
from mailing.forms import AddMailingSetingsForm, StyleForm
from mailing.models import MailingMessage, MailingSettings


class MailingMessageCreateView(TitleMixin, CreateView):
    model = MailingMessage
    form_class = StyleForm
    success_url = reverse_lazy('mailing:list')
    title = 'Создание сообщения'


class MailingMessageUpdateView(TitleMixin, UpdateView):
    model = MailingMessage
    form_class = StyleForm
    success_url = reverse_lazy('mailing:list')
    title = 'Редактирование сообщения'


class MailingMessageDeleteView(TitleMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')
    title = 'Удаление сообщения'


class MailingMessageListView(TitleMixin, ListView):
    model = MailingMessage
    title = 'Список сообщений'


class MailingMessageDetailView(TitleMixin, DetailView):
    model = MailingMessage
    from_class = StyleForm
    title = 'Просмотр сообщения'


class MailingSettingsCreateView(TitleMixin, CreateView):
    model = MailingSettings
    form_class = AddMailingSetingsForm
    success_url = reverse_lazy('mailing:settings_list')
    title = 'Добавление рассылки'


class MailingSettingsUpdateView(TitleMixin, UpdateView):
    model = MailingSettings
    form_class = AddMailingSetingsForm
    success_url = reverse_lazy('mailing:settings_list')
    title = 'Редактирование рассылки'


class MailingSettingsListView(TitleMixin, ListView):
    model = MailingSettings
    title = 'Планирование рассылки'


class MailingSettingsDetailView(TitleMixin, DetailView):
    model = MailingSettings
    title = 'Просмотр рассылки'


class MailingSettingsDeleteView(TitleMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')
    title = 'Удаление рассылки'
