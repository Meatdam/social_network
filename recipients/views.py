from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

from common.views import TitleMixin
from recipients.forms import AddRecipientsForm
from recipients.models import Recipients


class RecipientTemplateView(TitleMixin, TemplateView):
    template_name = "recipients/index.html"
    title = "Главная"


class RecipientCreateView(TitleMixin, CreateView):
    model = Recipients
    form_class = AddRecipientsForm
    title = 'Обратная связь'
    success_url = reverse_lazy('recipients:index')


class RecipientListView(TitleMixin, ListView):
    model = Recipients
    title = 'Список получателей'


class RecipientDetailView(TitleMixin, DetailView):
    model = Recipients
    success_url = reverse_lazy('recipients:list')
    title = 'Просмотр получателя'


class RecipientUpdateView(TitleMixin, UpdateView):
    model = Recipients
    form_class = AddRecipientsForm
    success_url = reverse_lazy('recipients:list')
    title = 'Редактирование получателя'


class RecipientDeleteView(TitleMixin, DeleteView):
    model = Recipients
    success_url = reverse_lazy('recipients:list')
    title = 'Удаление получателя'

