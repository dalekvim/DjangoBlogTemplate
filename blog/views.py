from django.shortcuts import render
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  DeleteView,
  FormView,
  TemplateView,
  UpdateView,
)
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class PostList(ListView):
  model = Post
  ordering = ['-date_posted']

class PostDetail(DetailView):
  model = Post

class CreatePost(CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class DeletePost(DeleteView):
  model = Post
  success_url = '/'

class UserProfile(TemplateView):
  model = User
  template_name = "accounts/profile.html"

class DetailedProfile(DetailView):
  model = User
  template_name = "accounts/profile.html"
  
class CreateUser(FormView):
  template_name = "registration/register.html"
  form_class = UserCreationForm
  success_url = '/accounts/login/'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['date_of_birth', 'bio']