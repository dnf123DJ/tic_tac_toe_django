

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class TicTacToeGame(models.Model):
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    current_player = models.CharField(max_length=50)
    board = models.CharField(max_length=9, default=" " * 9)
    winner = models.CharField(max_length=50, blank=True, null=True)
    is_draw = models.BooleanField(default=False)
    moves = models.IntegerField(default=0)
    played_date = models.DateTimeField(auto_now_add=True)
    game_state = models.TextField(default='')
    log = models.TextField(default='')

    def __str__(self):
        return f"{self.player1} vs {self.player2}"
