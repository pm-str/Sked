from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    email = models.EmailField()
    date_joined = models.DateField(auto_created=True)
    about = models.TextField(blank=True)
    token = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name
