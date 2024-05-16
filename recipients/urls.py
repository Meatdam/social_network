from django.urls import path

from recipients.apps import RecipientsConfig
from recipients.views import RecipientTemplateView, RecipientCreateView, RecipientListView, RecipientDetailView, \
    RecipientUpdateView, RecipientDeleteView

app_name = RecipientsConfig.name

urlpatterns = [
    path('', RecipientTemplateView.as_view(), name='index'),
    path('list/', RecipientListView.as_view(), name='list'),
    path('create/', RecipientCreateView.as_view(), name='create'),
    path('<int:pk>/', RecipientDetailView.as_view(), name='view'),
    path('<int:pk>/update/', RecipientUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', RecipientDeleteView.as_view(), name='delete'),
    ]