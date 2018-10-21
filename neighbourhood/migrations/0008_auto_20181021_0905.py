# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0007_business_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood'),
        ),
    ]