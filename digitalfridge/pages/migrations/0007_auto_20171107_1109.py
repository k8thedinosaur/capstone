# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20171107_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Fruit', 'Fruit'), ('Veg', 'Veg'), ('Meat', 'Meat'), ('Unknown', 'Unknown')], default='Unknown', max_length=20),
        ),
    ]
