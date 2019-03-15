from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=255, blank=False)
    hcp = models.IntegerField(blank=False)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)

class Team(models.Model):
    team1 = '1'
    team2 = '2'
    team3 = '3'
    team4 = '4'

    TEAMS = (
        (team1, team1),
        (team2, team2),
        (team3, team3),
        (team4, team4)
    )

    name = models.CharField(max_length=50, choices=TEAMS, null=False)
    scorecard = models.ForeignKey('Scorecard', on_delete=models.SET_NULL, null=True)

    def calculate_teamscores(self):
        pass

class Holes(models.Model):
    par = models.IntegerField()
    kp = models.BooleanField(default=False)
    hcp = models.IntegerField()

class Game(models.Model):
    game_count = models.IntegerField()
    press = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, null=True, blank=True)


class Scorecard(models.Model):
    players = models.ManyToManyField(Player)
    holes = models.ManyToManyField(Holes)

    games = models.ManyToManyField(Game)
    current_hole = models.IntegerField()
