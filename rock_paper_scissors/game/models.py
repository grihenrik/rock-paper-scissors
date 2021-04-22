# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from enum import IntEnum
from django.db import models
from django.conf import settings

NUMBER_OF_CHOICES = 3


class PlayerAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class Score(models.Model):
    user_choice = models.CharField(
      max_length=NUMBER_OF_CHOICES,
      choices=[(tag, tag.value) for tag in PlayerAction]
    )
    computer_choice = models.CharField(
      max_length=NUMBER_OF_CHOICES,
      choices=[(tag, tag.value) for tag in PlayerAction]
    )
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return [self.user_choice,
                self.computer_choice,
                self.created]
        

