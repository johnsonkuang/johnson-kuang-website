from django.db import models

# Create your models here.

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
    players = models.ManyToManyField('Person', through='Player')

    def calculate_teamscores(self):
        pass

'''
Usage:

Player.objects.add_player(user, team, *other_fields)
You will then be able to get User related Team, for example:

team_with_user = Team.objects.filter(players__name="hello")
user_in_team = User.objects.filter(team__name="world")
'''


class Person(models.Model):
    name = models.CharField(max_length=255, blank=False)
    hcp = models.IntegerField(blank=False)


class PlayerManager(models.Manager):
    use_for_related_fields = True
    def add_player(self, player, team):
        player.team = team
        player.save()

    def remove_player(self, player, team):
        player.team = None
        player.save()

    def transfer_player(self, player, team):
        player.team = team
        player.save()

    def clear_team(self, team):
        people_in_team = Person.objects.filter(team__name=team.name)
        for person in people_in_team:
            person.Player.clear_team()

class Player(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, blank=False, related_name='Player')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    objects = PlayerManager()
    #clears the team the player ahs been assigned to
    def clear_team(self):
        self.team = None
        self.save()



class Holes(models.Model):
    par = models.IntegerField()
    kp = models.BooleanField(default=False)
    hcp = models.IntegerField()


class Game(models.Model):
    game_count = models.IntegerField()
    press = models.BooleanField(default=False)
    winner = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)


class GameInfo(models.Model):
    game_name = models.CharField(max_length=255)
    num_players = models.IntegerField(max_length=255, null=True, blank=True)

    #before saving, attach object being passed to a Scorecard object
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        s = Scorecard.objects.create(game_info=self)
        s.save()
        self.save()

class Scorecard(models.Model):
    game_info = models.OneToOneField(GameInfo, on_delete=models.CASCADE, primary_key=True)
    players = models.ManyToManyField(Player, blank=True)
    holes = models.ManyToManyField(Holes, blank=True)

    games = models.ManyToManyField(Game, blank=True)
    current_hole = models.IntegerField(max_length=255, blank=True)
