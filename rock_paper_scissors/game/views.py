# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Welcome to a game of Rock, Paper and Scissors!")
