# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 19:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171103_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fridge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='pages.Fridge'),
        ),
    ]
