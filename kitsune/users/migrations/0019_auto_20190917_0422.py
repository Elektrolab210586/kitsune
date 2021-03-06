# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-17 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_codename'),
        ('users', '0018_change_bn_BD_and_bn_IN_to_bn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='has_subscriptions',
        ),
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(related_name='subscribed_users', to='products.Product'),
        ),
    ]
