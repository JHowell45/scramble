from django.contrib import admin

from .models import Character

# Register your models here.


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "avatar_tag",
        "strength",
        "magic",
        "dexterity",
        "created_at",
        "updated_at",
    ]
    date_hierarchy = "created_at"
