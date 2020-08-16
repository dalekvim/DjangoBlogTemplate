from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from .models import Post, Profile
from django.contrib.auth.models import User

# Create your views here.
class PostList(ListView):
  model = Post

class PostDetail(DetailView):
  model = Post

class CreatePost(CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  

class UserProfile(TemplateView):
  model = User
  template_name = "accounts/profile.html"