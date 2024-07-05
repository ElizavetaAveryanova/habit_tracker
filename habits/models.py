from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Reward(models.Model):
    """Вознаграждение действием"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=100, verbose_name="Название вознаграждения")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"


class Habit(models.Model):
    """Привычка """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец привычки")
    action = models.CharField(max_length=150, verbose_name="Действие")
    place = models.CharField(max_length=100, verbose_name="Место выполнения привычки", **NULLABLE)
    time = models.TimeField(verbose_name="Время выполнения привычки")
    period = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность выполнения в днях')
    duration = models.DurationField(default=None, verbose_name="Продолжительность выполнения в секундах")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")
    is_pleasing_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    #  варианты вознаграждения
    reward_with_action = models.ForeignKey(Reward, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Вознаграждение действием')
    reward_with_pleasing_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Вознаграждение приятной привычкой')
    def __str__(self):
        return f'Привычка: {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
