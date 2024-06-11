from django import forms

from common.views import StyleFormMixin
from mailing.models import MailingSettings, MailingMessage
from recipients.models import Recipients


class AddMailingSetingsForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для работы с формой "AddMailingSetingsForm" для рассылки
    """
    def __init__(self, *args, **kwargs):
        """
        Фильтрация в форме. Вывод только тех клиентов и сообщений которые
        принадлежать пользователю
        """
        self.request = kwargs.pop("request")
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields["recipients"].queryset = Recipients.objects.filter(owner=user)
        self.fields["message"].queryset = MailingMessage.objects.filter(owner=user)

    class Meta:
        model = MailingSettings
        fields = ['end_time', 'sending_period', 'message', 'recipients', 'settings_status']


class StyleForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для работы с формой "StyleForm"
    """
    class Meta:
        model = MailingMessage
        fields = ('title', 'content')


class ModeratorMailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модератора рассылки.
    """
    class Meta:
        model = MailingSettings
        fields = ('settings_status',)
