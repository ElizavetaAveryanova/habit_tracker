from django.db import models

NULLABLE = {"blank": True, "null": True}


class Reward(models.Model):
    """Вознаграждение действием"""

    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, **NULLABLE, verbose_name="Автор"
    )
    title = models.CharField(max_length=100, verbose_name="Название вознаграждения")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"


class Place(models.Model):
    """Место"""

    title = models.CharField(max_length=20, verbose_name="Название")
    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, **NULLABLE, verbose_name="Автор"
    )

    def __str__(self):
        return f"Место: {self.title}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Habit(models.Model):
    """Привычка"""

    place = models.ForeignKey(
        Place, on_delete=models.SET_NULL, null=True, verbose_name="Место выполнения"
    )
    time = models.TimeField(verbose_name="Время выполнения")
    action = models.CharField(max_length=250, verbose_name="Действие")
    period = models.PositiveSmallIntegerField(
        default=1, verbose_name="Периодичность выполнения в днях"
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name="Продолжительность выполнения в секундах"
    )
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")
    is_pleasing_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, **NULLABLE, verbose_name="Автор"
    )
    last_reminder = models.DateTimeField(
        **NULLABLE, verbose_name="Дата отправки последнего напоминания"
    )

    #  варианты вознаграждения
    reward_with_action = models.ForeignKey(
        Reward,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Вознаграждение действием",
    )
    reward_with_pleasing_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Вознаграждение приятной привычкой",
    )

    def __str__(self):
        return f"Привычка: {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
