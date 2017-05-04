# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    JOBS = (
        ('J', 'Jedi'),
        ('S', 'Smuggler'),
        ('B', 'Bounty hunter'),
        ('P', 'Politician'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    job = models.CharField(max_length=1, choices=JOBS)

    def __str__(self):
        return self.name
