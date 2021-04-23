# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models

# @admin.register(models.PlayerChoice)
# class PlayerChoiceAdmin(admin.ModelAdmin):
#     list_display = ['all']
#     list_filter = ['all']

admin.site.register(models.Score)
admin.site.register(models.PlayerChoice)
