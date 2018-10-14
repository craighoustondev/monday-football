from django.db import models

# Create your models here.
class Player(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    image = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Match(models.Model):
    date = models.DateField()
    cost = models.FloatField(default=0)

    def __str__(self):
        return self.date.strftime("%d %B %Y")

    class Meta:
        ordering = ['date']

class Appearance(models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.match) + " - " + str(self.player)

    class Meta:
        ordering = ['match', 'player']
        unique_together = (('match', 'player'),)
