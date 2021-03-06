# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('expires', models.DateField()),
                ('calories', models.CharField(blank=True, max_length=10, null=True)),
                ('intended_use', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
