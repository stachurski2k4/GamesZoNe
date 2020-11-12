from django.db import models
from django.contrib import auth
from django.urls import reverse_lazy,reverse
from django.conf import settings
# Create your models here.

class User(auth.models.User):
    image=models.ImageField(blank=True,upload_to='profile_pics/')
    description=models.TextField(blank=True)
    authorization_level=models.IntegerField(default=0)
    creted_date=models.DateField(auto_now=True)
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        super().set_password(self.password)
        return reverse('accounts:profile', kwargs={'pk': self.pk})
