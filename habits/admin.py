from django.contrib import admin

from habits.models import Habit, Reward, Place


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "created_by",
        "place",
        "time",
        "period",
        "duration",
        "is_public",
        "is_pleasing_habit",
        "last_reminder",
        "reward_with_action",
        "reward_with_pleasing_habit",
    )


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_by",
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_by",
    )
