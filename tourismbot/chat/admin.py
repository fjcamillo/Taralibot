from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.chatusers)
admin.site.register(models.conversations)
admin.site.register(models.destinations)
admin.site.register(models.services)