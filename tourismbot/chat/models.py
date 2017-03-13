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
    description = models.CharField(max_length=1000, default='Description')
    website = models.CharField(max_length=100, default='www.taralibot.xyz')
    imageUrls = post.JSONField(default="{default: none}")
    image_one = models.ImageField(null=True)
    image_two = models.ImageField(null=True)
    image_three = models.ImageField(null=True)
    image_four = models.ImageField(null=True)
    image_five = models.ImageField(null=True)
    address = models.CharField(max_length=100, default="PUP Sta.Mesa")
    contact_number = models.CharField(max_length=20, default="0")


class services(models.Model):
    destinations_fk = models.ForeignKey(destinations, on_delete=models.CASCADE)
    list_services = post.JSONField()

class chatusers(models.Model):
    facebook_id = models.CharField(max_length=100)
    facebook_image = models.ImageField(null=True)
    facebook_name = models.CharField(max_length=100, default='name')

class conversations(models.Model):
    facebook_fk = models.ForeignKey(chatusers, on_delete=models.CASCADE)
    converse = models.CharField(max_length=320)
    timestamp = models.DateTimeField(auto_now=True)

class user_accounts(models.Model):
    username = models.CharField(max_length=50, default='username')
    password = models.CharField(max_length=100, default='passwords')
    email_address = models.CharField(max_length=50, default='taralibot@gmail.com')
    facebook_connected_id = models.ForeignKey(chatusers, on_delete=models.CASCADE)
    age = models.IntegerField()
    image = models.ImageField(null=True)

