from django.urls import path
from blog.views import UserProfile, DetailedProfile, CreateUser, ProfileUpdate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('register/', CreateUser.as_view(extra_context = {'title': 'Sign Up'}), name='register'),
  path('login/', LoginView.as_view(extra_context = {'title': 'Login'}), name='login'),
  path('logout/', LogoutView.as_view(extra_context = {'title': 'Logout'}, template_name="registration/logout.html"), name='logout'),
  path('profile/', login_required(UserProfile.as_view(extra_context = {'title': 'Your Profile'}))),
  path('profile/<int:pk>/', login_required(DetailedProfile.as_view()), name="profile"),
  path('profile/<int:pk>/update/', login_required(ProfileUpdate.as_view(extra_context = {'title': 'Profile Update'})), name="profile-update"),
]
