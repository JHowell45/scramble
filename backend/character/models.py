from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(
        upload_to="characters/avatars/%Y/%m/%d/",
        default="characters/avatars/default.jpg",
    )
    strength = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    magic = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    dexterity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    current_health = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
