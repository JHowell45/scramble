from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(
        upload_to="characters/avatars/%Y/%m/%d/",
        default="characters/avatars/default.jpg",
    )
    strength = models.IntegerField()
    magic = models.IntegerField()
    dexterity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    current_health = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
