from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from blog.forms import BlogAddForm
from blog.models import Blog
from common.views import TitleMixin


class BlogListView(TitleMixin, ListView):
    """
    Класс для отображения всех постов.
    """
    model = Blog
    title = 'Все посты'


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, CreateView):
    """
    Класс для добавления поста.
    """
    model = Blog
    title = 'Добавить пост'
    permission_required = 'blog.add_blog'
    form_class = BlogAddForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        """
        Привязывание поста к текущему пользователю.
        """
        post = form.save()
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)


class BlogDetailView(TitleMixin, DetailView):
    """
    Класс для просмотра деталей поста.
    """
    model = Blog
    title = 'Просмотр поста'

    def get_object(self, queryset=None):
        """
        Увеличивает количество просмотров поста.
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Класс для удаления поста.
    """
    model = Blog
    title = 'Удаление поста'
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(TitleMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Класс для редактирования поста.
    """
    model = Blog
    title = 'Редактирование поста'
    permission_required = 'blog.change_blog'
    form_class = BlogAddForm

    def get_success_url(self, **kwargs):
        """
        Переопределение метода "get_success_url" для перехода на страницу поста
        :return: reverse_lazy('blog:view', kwargs={'pk': self.get_object().id})
        """
        return reverse_lazy('blog:detail_blog', kwargs={'pk': self.get_object().id})
