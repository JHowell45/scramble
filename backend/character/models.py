from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class Character(models.Model):
    class StatChoices(models.IntegerChoices):
        STRONG = 4
        AVERAGE = 3
        WEAK = 1

    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(
        upload_to="characters/avatars/%Y/%m/%d/",
        default="characters/avatars/default.jpg",
    )
    strength = models.IntegerField(
        choices=StatChoices.choices,
    )
    magic = models.IntegerField(
        choices=StatChoices.choices,
    )
    dexterity = models.IntegerField(
        choices=StatChoices.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def avatar_tag(self):
        """Loads the actual image into a HTML tag with the image URL."""
        return mark_safe(
            f'<img src="{settings.MEDIA_URL}{self.avatar}" width="150" height="150" />'
        )


class Player(models.Model):
    name = models.CharField(max_length=100)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    current_health = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
