# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-05 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='', upload_to='pictures'),
        ),
    ]