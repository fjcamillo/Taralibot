from __future__ import unicode_literals

from django.db import models
import django.contrib.postgres.fields as post
# Create your models here.

class destinations(models.Model):
    name = models.CharField(max_length=40)
    longitude = models.FloatField()
    latitude = models.FloatField()
    defaultimage = models.ImageField(null=True)
    owner = models.CharField(max_length=20)

class services(models.Model):
    destinations_fk = models.ForeignKey(destinations, on_delete=models.CASCADE)
    list_services = post.JSONField()

class chatusers(models.Model):
    facebook_id = models.CharField(max_length=100)
    facebook_image = models.ImageField(null=True)

class conversations(models.Model):
    facebook_fk = models.ForeignKey(chatusers, on_delete=models.CASCADE)
    converse = models.CharField(max_length=320)