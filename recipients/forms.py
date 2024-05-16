from django import forms

from common.views import StyleFormMixin
from recipients.models import Recipients


class AddRecipientsForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для работы с формой "AddPostForm"
    """
    class Meta:
        model = Recipients
        fields = ['email', 'name', 'description']




