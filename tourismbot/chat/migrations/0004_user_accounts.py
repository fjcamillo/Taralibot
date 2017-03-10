# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20170309_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=50)),
                ('password', models.CharField(default='passwords', max_length=100)),
                ('email_address', models.CharField(default='taralibot@gmail.com', max_length=50)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('facebook_connected_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatusers')),
            ],
        ),
    ]
