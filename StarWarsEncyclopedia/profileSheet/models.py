# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
