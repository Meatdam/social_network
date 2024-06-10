from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from common.views import TitleMixin
from mailing.models import MailingSettings
from recipients.forms import AddRecipientsForm
from recipients.models import Recipients
from recipients.services import get_blog_from_cache


class RecipientTemplateView(TitleMixin, TemplateView):
    template_name = "recipients/index.html"
    title = "Главная"

    def get_context_data(self, **kwargs):
        """
        Добавление заголовка в контекст
        """
        context_data = super().get_context_data(**kwargs)

        context_data['blog'] = get_blog_from_cache()

        mailing_settings = MailingSettings.objects.all()
        context_data['mailing_settings'] = len(mailing_settings)

        active_mailings = MailingSettings.objects.filter(settings_status='Started')
        context_data['active_mailings'] = len(active_mailings)

        recipients = Recipients.objects.all()
        context_data['recipient'] = len(recipients)
        return context_data


class RecipientCreateView(TitleMixin, LoginRequiredMixin, CreateView):
    """
    Класс для работы с формой "AddRecipientsForm" для добавления получателя
    """
    model = Recipients
    form_class = AddRecipientsForm
    title = 'Добавление получателя'
    success_url = reverse_lazy('recipients:index')

    def form_valid(self, form):
        """
        Привязка клиента к текущему менеджеру
        """
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)


class RecipientListView(TitleMixin, LoginRequiredMixin, ListView):
    """
    Класс для просмотра списка получателей
    """
    model = Recipients
    title = 'Список получателей'


class RecipientDetailView(TitleMixin, LoginRequiredMixin, DetailView):
    """
    Класс для просмотра деталей получателя
    """
    model = Recipients
    success_url = reverse_lazy('recipients:list')
    title = 'Просмотр получателя'


class RecipientUpdateView(TitleMixin, LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования получателя
    """
    model = Recipients
    form_class = AddRecipientsForm
    title = 'Редактирование получателя'

    def get_success_url(self):
        """
        Переопределение метода "get_success_url" для перехода на страницу получателя
        :return: reverse_lazy('recipients:view', kwargs={'pk': self.get_object().id})
        """
        return reverse_lazy('recipients:view', kwargs={'pk': self.get_object().id})


class RecipientDeleteView(TitleMixin, LoginRequiredMixin, DeleteView):
    """
    Класс для удаления получателя
    """
    model = Recipients
    success_url = reverse_lazy('recipients:list')
    title = 'Удаление получателя'
