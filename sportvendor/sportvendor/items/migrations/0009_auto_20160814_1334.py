# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20160814_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
