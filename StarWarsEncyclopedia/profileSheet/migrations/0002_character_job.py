# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileSheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='job',
            field=models.CharField(choices=[('J', 'Jedi'), ('B', 'Bounty hunter'), ('P', 'Politician')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
