# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0005_business_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
    ]