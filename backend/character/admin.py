from django.contrib import admin

from .models import Character, Player

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
