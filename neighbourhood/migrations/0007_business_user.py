# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0006_remove_business_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Profile'),
        ),
    ]
