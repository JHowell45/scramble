from character.models import Player
from django.db import models


# Create your models here.
class GameState(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name="players")
    current_chapter = models.IntegerField(default=1)
    at_boss_card = models.BooleanField(default=False)
    game_beaten = models.BooleanField(default=False)
    game_lost = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
