from django import forms

from blog.models import Blog
from common.views import StyleFormMixin


class BlogAddForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для работы с формой добавление поста
    """
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', )
