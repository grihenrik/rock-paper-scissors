# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enum import IntEnum
from django.db import models
from django.conf import settings


class PlayerAction(IntEnum):
  """Enum class for handling winning and loosing"""
  Rock = 1
  Paper = 2
  Scissors = 3
  
        

class PlayerChoice(models.Model):
  """
    Base model for player choice
  """
  user_choice = models.CharField(max_length=50)
  def __str__(self):
    return self.user_choice
