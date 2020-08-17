from django.urls import path
from .views import PostList, PostDetail, CreatePost, DeletePost
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('', PostList.as_view(extra_context = {'title': 'Blog Home'}), name='home'),
  path('post/<int:pk>/', PostDetail.as_view(extra_context = {'title': 'Post Detail'}), name='post'),
  path('create/', login_required(CreatePost.as_view(extra_context = {'title': 'Create'})), name='create'),
  path('delete/<int:pk>/', login_required(DeletePost.as_view(extra_context = {'title': 'Delete'})), name='delete'),
]
