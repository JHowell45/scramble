from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.IntegerField()
    magic = models.IntegerField()
    dexterity = models.IntegerField()
    health = models.IntegerField()