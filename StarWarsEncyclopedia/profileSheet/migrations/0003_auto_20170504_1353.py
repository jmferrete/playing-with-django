# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileSheet', '0002_character_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]