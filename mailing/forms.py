from django import forms

from common.views import StyleFormMixin
from mailing.models import MailingSettings, MailingMessage


class AddMailingSetingsForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].empty_label = "Сообщение не выбрано"

    class Meta:
        model = MailingSettings
        fields = ['end_time', 'sending_period', 'message', 'recipients', 'settings_status']


class StyleForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('title', 'content')


