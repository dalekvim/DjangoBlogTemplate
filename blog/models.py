from django.db import models
from django.db.models import Model, CharField, ForeignKey, DateTimeField, OneToOneField, DateField
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Post(Model):
  title = CharField(max_length=150)
  author = ForeignKey(User, on_delete=models.CASCADE)
  date_posted = DateTimeField(default=timezone.now)
  content = HTMLField()

  def get_absolute_url(self):
      return reverse("post_detail", kwargs={"pk": self.pk})
  

class Profile(Model):
  user = OneToOneField(User, on_delete=models.CASCADE)
  date_of_birth = DateField()
  bio = HTMLField()