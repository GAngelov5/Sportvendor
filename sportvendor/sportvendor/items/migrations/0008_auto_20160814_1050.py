# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20160814_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='images/img-thing.jpg', upload_to='images/'),
        ),
    ]
