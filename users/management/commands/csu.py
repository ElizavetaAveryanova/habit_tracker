import os

from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Создание superuser"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@habits.ru",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.save()

