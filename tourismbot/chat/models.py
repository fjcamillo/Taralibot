from __future__ import unicode_literals

from django.db import models
import django.contrib.postgres.fields as post
# Create your models here.

class destinations(models.Model):
    name = models.CharField(max_length=40)
    longitude = models.FloatField()
    latitude = models.FloatField()
    services = post.JSONField()
    
