from django.db import models

# Create your models here.
class Player(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Match(models.Model):
    date = models.DateField()
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.date.strftime("%d %B %Y")

class Appearance(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    paid = models.BooleanField()

    def __str__(self):
        return str(self.match) + " - " + str(self.player)
