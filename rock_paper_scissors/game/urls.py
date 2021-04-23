from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="game/index.html"), name='game'),
    path('<int:choice_id>', views.user_choice, name='user_choice'),
    
]