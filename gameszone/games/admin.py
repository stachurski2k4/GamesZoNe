from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Game)
admin.site.register(models.Comment)
admin.site.register(models.Version)
admin.site.register(models.ScreenShot)