<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        verbose_name="Почта", unique=True, help_text="Укажите почту"
    )
    chat_id = models.CharField(
        max_length=20, **NULLABLE, verbose_name="chat id телеграмма"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
=======
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        verbose_name="Почта", unique=True, help_text="Укажите почту"
    )
    chat_id = models.CharField(
        max_length=20, **NULLABLE, verbose_name="chat id телеграмма"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
