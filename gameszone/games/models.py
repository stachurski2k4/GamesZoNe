from django.db import models
from accounts.models import User
from django.shortcuts import reverse
# Create your models here.
class Game(models.Model):
    title=models.CharField(max_length=64)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='games_icons/')
    status=models.CharField(max_length=30)
    description=models.TextField(blank=True,max_length=3000)
    downloads_count=models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('games:game',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title

class Version(models.Model):
    game=models.ForeignKey(Game,related_name='versions', on_delete=models.CASCADE)
    download=models.FileField(upload_to='games_versions/')
    creted_date=models.DateField(auto_now=True)
    version_str=models.CharField(max_length=30)

    def __str__(self):
        return self.game.title
        
class ScreenShot(models.Model):
    game=models.ForeignKey(Game,related_name='screens', on_delete=models.CASCADE)
    image=models.ImageField(blank=True,upload_to='games_screens/')
    def __str__(self):
        return self.game.title

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    game=models.ForeignKey(Game,related_name='comments', on_delete=models.CASCADE)
    creted_date=models.DateField(auto_now=True)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.author.username