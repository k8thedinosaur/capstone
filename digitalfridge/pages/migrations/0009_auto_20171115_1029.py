# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tossed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('Meat', 'Meat'), ('Seafood', 'Seafood'), ('Dairy', 'Dairy'), ('Veg', 'Veg'), ('Fruit', 'Fruit'), ('Leftovers', 'Leftovers'), ('Alcohol', 'Alcohol'), ('Non-Edible', 'Non-Edible'), ('Other', 'Other'), ('Condiments', 'Condiments'), ('Sauces', 'Sauces'), ('Beverages', 'Beverages'), ('Frozen', 'Frozen'), ('Heat-n-Eat', 'Heat-n-Eat'), ('Desserts', 'Desserts')], default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='fridge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fridge', to='pages.Fridge'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity/Servings'),
        ),
    ]
