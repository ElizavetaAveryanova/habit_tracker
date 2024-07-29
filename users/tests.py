<<<<<<< HEAD
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_register_user(self):
        """Тестирование регистрации пользователя"""
        data = {
            "email": "test@mail.ru",
            "password": "ASDFGTREWQ",
            "password2": "ASDFGTREWQ",
            "chat_id": "1234567890",
            "first_name": "Test",
            "last_name": "Testovich",
        }

        response = self.client.post(reverse("users:register"), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(1, User.objects.all().count())

    def test_register_user_bad_password2(self):
        """Тестирование регистрации пользователя"""
        data = {
            "email": "test@mail.ru",
            "password": "ASDFGTREWQ",
            "password2": "A",
            "chat_id": "1234567890",
            "first_name": "Test",
            "last_name": "Testovich",
        }

        response = self.client.post(reverse("users:register"), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
=======
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_register_user(self):
        """Тестирование регистрации пользователя"""
        data = {
            "email": "test@mail.ru",
            "password": "ASDFGTREWQ",
            "password2": "ASDFGTREWQ",
            "chat_id": "1234567890",
            "first_name": "Test",
            "last_name": "Testovich",
        }

        response = self.client.post(reverse("users:register"), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(1, User.objects.all().count())

    def test_register_user_bad_password2(self):
        """Тестирование регистрации пользователя"""
        data = {
            "email": "test@mail.ru",
            "password": "ASDFGTREWQ",
            "password2": "A",
            "chat_id": "1234567890",
            "first_name": "Test",
            "last_name": "Testovich",
        }

        response = self.client.post(reverse("users:register"), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
