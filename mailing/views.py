from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.views import TitleMixin
from mailing.forms import AddMailingSetingsForm, StyleForm, ModeratorMailingSettingsForm
from mailing.models import MailingMessage, MailingSettings, MailingStatus


class MailingMessageCreateView(TitleMixin, LoginRequiredMixin, CreateView):
    """
    Класс для создания сообщения для рассылки
    """
    model = MailingMessage
    form_class = StyleForm
    success_url = reverse_lazy('mailing:list')
    title = 'Создание сообщения'

    def form_valid(self, form):
        """
        Привязка сообщение к текущему пользователю.
        """
        mailingmessage = form.save()
        mailingmessage.owner = self.request.user
        mailingmessage.save()
        return super().form_valid(form)


class MailingMessageUpdateView(TitleMixin, LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования сообщения для рассылки
    """
    model = MailingMessage
    form_class = StyleForm
    success_url = reverse_lazy('mailing:list')
    title = 'Редактирование сообщения'

    def get_success_url(self, **kwargs):
        """
        Переопределение метода "get_success_url" для перехода на страницу сообщения
        :return: reverse_lazy('mailing:view', kwargs={'pk': self.get_object().id})
        """
        return reverse_lazy('mailing:view', kwargs={'pk': self.get_object().id})


class MailingMessageDeleteView(TitleMixin, LoginRequiredMixin, DeleteView):
    """
    Класс для удаления сообщения рассылки
    """
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')
    title = 'Удаление сообщения'


class MailingMessageListView(TitleMixin, LoginRequiredMixin, ListView):
    """
    Класс для просмотра списка сообщений рассылки
    """
    model = MailingMessage
    title = 'Список сообщений'


class MailingMessageDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    """
    Класс для просмотра деталий сообщения рассылки
    """
    model = MailingMessage
    from_class = StyleForm
    title = 'Просмотр сообщения'


class MailingSettingsCreateView(TitleMixin, LoginRequiredMixin, CreateView):
    """
    Класс для создания рассылки
    """
    model = MailingSettings
    form_class = AddMailingSetingsForm
    success_url = reverse_lazy('mailing:settings_list')
    title = 'Добавление рассылки'

    def get_form_kwargs(self):
        """
        Приминение фильтрации в форме на создание рассылки
        """
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        """
        Привязывает рассылку к текущему пользователю.
        """
        mailing_settings = form.save()
        mailing_settings.owner = self.request.user
        mailing_settings.save()

        return super().form_valid(form)


class MailingSettingsUpdateView(TitleMixin, LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования рассылки
    """
    model = MailingSettings
    form_class = AddMailingSetingsForm
    title = 'Редактирование рассылки'

    def get_success_url(self, **kwargs):
        """
        Переопределение метода "get_success_url" для перехода на страницу рассылки
        :return: reverse_lazy('mailing:settings_view', kwargs={'pk': self.get_object().id})
        """
        mailing_settings = self.get_object()
        return reverse_lazy('mailing:settings_view', kwargs={'pk': mailing_settings.id})

    def get_form_class(self):
        """
        Переопределение метода "get_form_class" для переопределения формы редактирования рассылки,
        отскрыть доступ для редактирования статуса для модератора
        """
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return AddMailingSetingsForm
        if user.has_perm('mailing.change_mailingsettings_settings_status'):
            return ModeratorMailingSettingsForm
        return PermissionDenied


class MailingSettingsListView(TitleMixin, LoginRequiredMixin, ListView):
    """
    Класс для просмотра списка рассылок
    """
    model = MailingSettings
    title = 'Планирование рассылки'
    permission_required = 'mailing.view_mailingsettings'


class MailingSettingsDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    """
    Класс для просмотра деталей рассылки
    """
    model = MailingSettings
    title = 'Просмотр рассылки'


class MailingSettingsDeleteView(TitleMixin, LoginRequiredMixin, DeleteView):
    """
    Класс для удаления рассылки
    """
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')
    title = 'Удаление рассылки'
    permission_required = 'mailing.delete_mailingsettings'


class MailingStatusListView(TitleMixin, LoginRequiredMixin, ListView):
    """
    Класс для просмотра списка статусов рассылки
    """
    model = MailingStatus
    title = 'Статус рассылки'


class MailingStatusDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    """
    Класс для просмотра деталей статуса рассылки
    """
    model = MailingStatus
    title = 'Статус рассылки'
