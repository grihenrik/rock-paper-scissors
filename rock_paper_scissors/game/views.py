# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import PlayerChoice, PlayerAction

VICTORIES = {
        PlayerAction.Rock: [PlayerAction.Scissors],  # Rock beats scissors
        PlayerAction.Paper: [PlayerAction.Rock],  # Paper beats rock
        PlayerAction.Scissors: [PlayerAction.Paper]  # Scissors beats paper
    }

def get_computer_selection():
    selection = random.randint(2, 4)
    return selection

def index(request):

    return render(request, 'game/index.html',{})

def user_choice(request, choice_id):
    try:
        uc = PlayerChoice.objects.get(pk=choice_id)
        pc = PlayerChoice.objects.get(pk=get_computer_selection())
        defeats = VICTORIES[uc.id]
        print(defeats, uc, pc)
        if uc == pc:
            resp = "Both players selected %s. It's a tie!"%uc
        elif pc.id in defeats:
            resp = "%s beats %s! You win!"%(uc,pc)
        else:
            resp = "%s beats %s! You lose."%(pc,uc)
    except PlayerChoice.DoesNotExist:
        raise Http404("Choice does not exist")
    return render(request, 'game/result.html',{"users_choice":uc,"computer_choice":pc,"win_loose":resp})
