# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Character

def index(request):
    character_list = Character.objects.order_by('name')
    template = loader.get_template('index.html')
    context = {
        'character_list': character_list,
    }
    return HttpResponse(template.render(context, request))

