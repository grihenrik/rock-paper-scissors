# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enum import IntEnum
from django.db import models
from django.conf import settings

NUMBER_OF_CHOICES = 3


class PlayerAction(IntEnum):
    Rock = 2
    Paper = 3
    Scissors = 4

class PlayerChoice(models.Model):
    user_choice = models.CharField(max_length=50)
    def __str__(self):
          return self.user_choice


