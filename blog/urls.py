from django.urls import path
from .views import PostList, PostDetail, CreatePost, DeletePost, UserProfile, DetailedProfile, CreateUser, ProfileUpdate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
  path('', PostList.as_view(extra_context = {'title': 'Blog Home'}), name='home'),
  path('post/<int:pk>/', PostDetail.as_view(extra_context = {'title': 'Post Detail'}), name='post'),
  path('create/', login_required(CreatePost.as_view(extra_context = {'title': 'Create'})), name='create'),
  path('delete/<int:pk>/', login_required(DeletePost.as_view(extra_context = {'title': 'Delete'})), name='delete'),
  path('accounts/register/', CreateUser.as_view(extra_context = {'title': 'Sign Up'}), name='register'),
  path('accounts/login/', LoginView.as_view(extra_context = {'title': 'Login'}), name='login'),
  path('accounts/logout/', LogoutView.as_view(extra_context = {'title': 'Logout'}, template_name="registration/logout.html"), name='logout'),
  path('accounts/profile/', login_required(UserProfile.as_view(extra_context = {'title': 'Your Profile'}))),
  path('accounts/profile/<int:pk>/', login_required(DetailedProfile.as_view()), name="profile"),
  path('accounts/profile/<int:pk>/update/', login_required(ProfileUpdate.as_view(extra_context = {'title': 'Profile Update'})), name="profile-update"),
]
