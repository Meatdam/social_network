from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>', BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail_blog/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='detail_blog'),
]