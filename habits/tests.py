import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Place, Reward, Habit
from users.models import User


class HabitTestCase(APITestCase):
    maxDiff = None
    email = "user@test.ru"
    password = "test_asdfg"
    chat_id = "123456789"
    email_2 = "user2@test.ru"
    password_2 = "test_gfdsa"
    chat_id_2 = "987654321"

    def setUp(self) -> None:
        self.user = User.objects.create(
            email=self.email, password=self.password, chat_id=self.chat_id
        )
        self.user.set_password(self.password)
        self.user.save()

        response = self.client.post(
            "/users/token/", {"email": self.email, "password": self.password}
        )
        self.token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.place = Place.objects.create(
            title="test_place", created_by=self.user
        )
        self.reward = Reward.objects.create(
            title="test_reward", created_by=self.user
        )
        self.habit = Habit.objects.create(
            place=self.place,
            time="22:00:00",
            action="делать массаж шеи",
            period=1,
            duration=120,
            is_pleasing_habit=False,
            reward_with_action=self.reward,
            created_by=self.user,
        )
        self.pleasing_habit = Habit.objects.create(
            place=self.place,
            time="23:00:00",
            action="ложиться спать",
            period=1,
            duration=60,
            is_pleasing_habit=True,
            created_by=self.user,
        )

        self.user_2 = User.objects.create(
            email=self.email_2, password=self.password_2, chat_id=self.chat_id_2
        )
        self.place_2 = Place.objects.create(
            title="test_place_2", created_by=self.user_2
        )
        self.reward_2 = Reward.objects.create(
            title="test_reward_2", created_by=self.user_2
        )
        self.habit_2 = Habit.objects.create(
            place=self.place_2,
            time="21:00:00",
            action="дыхательная гимнастика",
            period=1,
            duration=120,
            is_pleasing_habit=False,
            reward_with_action=self.reward_2,
            created_by=self.user_2,
            is_public=True,
        )

    #  тесты модели Place
    def test_create_place(self):
        """Тестирование создания места"""
        url = reverse("habits:place-list")
        data = {
            "title": "place",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Place.objects.count(), 3)
        self.assertEqual(Place.objects.last().created_by, self.user)

    def test_getting_place_list(self):
        """Тестирование вывода списка мест для пользователя"""
        url = reverse("habits:place-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.place.id,
                    "title": self.place.title,
                    "created_by": self.place.created_by_id,
                }
            ],
        )

    def test_getting_place_by_owner(self):
        """Тестирование вывода места для пользователя: автор"""
        url = reverse("habits:place-detail", args=[self.place.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": self.place.id,
                "title": self.place.title,
                "created_by": self.place.created_by_id,
            },
        )


    def test_getting_place_by_no_owner(self):
        """Тестирование вывода места для пользователя: не автор"""
        url = reverse("habits:place-detail", args=[self.place_2.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_place_by_owner(self):
        """Тестирование изменения места: автор"""
        url = reverse("habits:place-detail", args=[self.place.pk])
        data = {
            "title": "place_updated",
            "created_by": self.user.pk,
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.place.refresh_from_db()
        self.assertEqual(self.place.title, data["title"])

    def test_update_place_by_no_owner(self):
        """Тестирование изменения места: не автор"""
        url = reverse("habits:place-detail", args=[self.place_2.pk])
        data = {
            "title": "place_updated",
            "created_by": self.user.pk,
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_place_by_owner(self):
        """Тестирование удаления места: автор"""
        url = reverse("habits:place-detail", args=[self.place.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Place.objects.count(), 1)

    def test_delete_place_by_no_owner(self):
        """Тестирование удаления места: не автор"""
        url = reverse("habits:place-detail", args=[self.place_2.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Place.objects.count(), 2)

    #  тесты модели Reward
    def test_create_reward(self):
        """Тестирование создания вознаграждения"""
        url = reverse("habits:reward-list")
        data = {
            "title": "reward",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reward.objects.count(), 3)
        self.assertEqual(Reward.objects.last().created_by, self.user)

    def test_getting_reward_list(self):
        """Тестирование вывода списка вознаграждений для пользователя"""
        url = reverse("habits:reward-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.reward.id,
                    "title": self.reward.title,
                    "created_by": self.reward.created_by_id,
                }
            ],
        )

    def test_getting_reward_by_owner(self):
        """Тестирование вывода вознаграждения для пользователя: автор"""
        url = reverse("habits:reward-detail", args=[self.reward.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": self.reward.id,
                "title": self.reward.title,
                "created_by": self.reward.created_by_id,
            },
        )

    def test_getting_reward_by_no_owner(self):
        """Тестирование вывода вознаграждения для пользователя: не автор"""
        url = reverse("habits:reward-detail", args=[self.reward_2.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_reward_by_owner(self):
        """Тестирование изменения вознаграждения: автор"""
        url = reverse("habits:reward-detail", args=[self.reward.pk])
        data = {
            "title": "reward_updated",
            "created_by": self.user.pk
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.reward.refresh_from_db()
        self.assertEqual(self.reward.title, data["title"])

    def test_update_reward_by_no_owner(self):
        """Тестирование изменения вознаграждения: не автор"""
        url = reverse("habits:reward-detail", args=[self.reward_2.pk])
        data = {
            "title": "reward_updated",
            "created_by": self.user.pk
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_reward_by_owner(self):
        """Тестирование удаления вознаграждения: автор"""
        url = reverse("habits:reward-detail", args=[self.reward.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reward.objects.count(), 1)

    def test_delete_reward_by_no_owner(self):
        """Тестирование удаления вознаграждения: не автор"""
        url = reverse("habits:reward-detail", args=[self.reward_2.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Reward.objects.count(), 2)

    #  тесты модели Habit
    def test_create_habit(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 1,
            "duration": 60,
            "is_pleasing_habit": False,
            "reward_with_action": self.reward.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 4)
        self.assertEqual(Habit.objects.last().created_by, self.user)

    def test_create_habit_incorrect_period(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 8,
            "duration": 60,
            "is_pleasing_habit": False,
            "reward_with_action": self.reward.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_incorrect_duration(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 1,
            "duration": 121,
            "is_pleasing_habit": False,
            "reward_with_action": self.reward.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_both_reward(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 1,
            "duration": 120,
            "is_pleasing_habit": False,
            "reward_with_action": self.reward.pk,
            "reward_with_pleasing_habit": self.pleasing_habit.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_no_reward(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 1,
            "duration": 120,
            "is_pleasing_habit": False,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_reward_for_pleasing_habit(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habit_create")
        data = {
            "place": self.place.pk,
            "time": "07:00:00",
            "action": "выпивать стакан воды",
            "period": 1,
            "duration": 120,
            "is_pleasing_habit": True,
            "reward_with_action": self.reward.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_getting_habit_list(self):
        """Тестирование вывода списка привычек пользователя"""
        url = reverse("habits:habit_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content)["results"],
            [
                {
                    "id": self.habit.id,
                    "place": self.habit.place_id,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "period": self.habit.period,
                    "duration": self.habit.duration,
                    "is_public": self.habit.is_public,
                    "is_pleasing_habit": self.habit.is_pleasing_habit,
                    "created_by": self.habit.created_by_id,
                    "last_reminder": self.habit.last_reminder,
                    "reward_with_action": self.habit.reward_with_action_id,
                    "reward_with_pleasing_habit": self.habit.reward_with_pleasing_habit_id,
                },
                {
                    "id": self.pleasing_habit.id,
                    "place": self.pleasing_habit.place_id,
                    "time": self.pleasing_habit.time,
                    "action": self.pleasing_habit.action,
                    "period": self.pleasing_habit.period,
                    "duration": self.pleasing_habit.duration,
                    "is_public": self.pleasing_habit.is_public,
                    "is_pleasing_habit": self.pleasing_habit.is_pleasing_habit,
                    "created_by": self.pleasing_habit.created_by_id,
                    "last_reminder": self.pleasing_habit.last_reminder,
                    "reward_with_action": self.pleasing_habit.reward_with_action_id,
                    "reward_with_pleasing_habit": self.pleasing_habit.reward_with_pleasing_habit_id,
                },
            ],
        )

    def test_getting_public_habit_list(self):
        """Тестирование вывода списка публичных привычек"""
        url = reverse("habits:public_habit_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.habit_2.id,
                    "place": self.habit_2.place_id,
                    "time": self.habit_2.time,
                    "action": self.habit_2.action,
                    "period": self.habit_2.period,
                    "duration": self.habit_2.duration,
                    "is_public": self.habit_2.is_public,
                    "is_pleasing_habit": self.habit_2.is_pleasing_habit,
                    "created_by": self.habit_2.created_by_id,
                    "last_reminder": self.habit_2.last_reminder,
                    "reward_with_action": self.habit_2.reward_with_action_id,
                    "reward_with_pleasing_habit": self.habit_2.reward_with_pleasing_habit_id,
                }
            ],
        )

    def test_getting_habit_by_owner(self):
        """Тестирование вывода привычки: автор"""

        url = reverse("habits:habit_get", args=(self.habit.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content),
            {
                "id": self.habit.id,
                "place": self.habit.place_id,
                "time": self.habit.time,
                "action": self.habit.action,
                "period": self.habit.period,
                "duration": self.habit.duration,
                "is_public": self.habit.is_public,
                "is_pleasing_habit": self.habit.is_pleasing_habit,
                "created_by": self.habit.created_by_id,
                "last_reminder": self.habit.last_reminder,
                "reward_with_action": self.habit.reward_with_action_id,
                "reward_with_pleasing_habit": self.habit.reward_with_pleasing_habit_id,
            },
        )

    def test_getting_habit_by_no_owner_is_public(self):
        """Тестирование вывода привычки: не автор"""

        url = reverse("habits:habit_get", args=(self.habit_2.pk,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            json.loads(response.content),
            {
                "id": self.habit_2.id,
                "place": self.habit_2.place_id,
                "time": self.habit_2.time,
                "action": self.habit_2.action,
                "period": self.habit_2.period,
                "duration": self.habit_2.duration,
                "is_public": self.habit_2.is_public,
                "is_pleasing_habit": self.habit_2.is_pleasing_habit,
                "created_by": self.habit_2.created_by_id,
                "last_reminder": self.habit_2.last_reminder,
                "reward_with_action": self.habit_2.reward_with_action_id,
                "reward_with_pleasing_habit": self.habit_2.reward_with_pleasing_habit_id,
            },
        )

    def test_update_habit_by_owner(self):
        """Тестирование изменения привычки: автор"""
        url = reverse("habits:habit_update", args=[self.habit.pk])
        data = {
            "place": self.habit.place_id,
            "time": self.habit.time,
            "action": "updated_action",
            "period": self.habit.period,
            "duration": self.habit.duration,
            "reward_with_action": self.habit.reward_with_action_id,
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, data["action"])

    def test_update_habit_by_no_owner(self):
        """Тестирование изменения привычки: не автор"""
        url = reverse("habits:habit_update", args=[self.habit_2.pk])
        data = {
            "place": self.habit_2.place_id,
            "time": self.habit_2.time,
            "action": "updated_action",
            "period": self.habit_2.period,
            "duration": self.habit_2.duration,
            "reward_with_action": self.habit_2.reward_with_action_id,
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_habit_by_owner(self):
        """Тестирование удаления привычки: автор"""
        url = reverse("habits:habit_delete", args=[self.habit.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 2)

    def test_delete_habit_by_no_owner(self):
        """Тестирование удаления привычки: не автор"""
        url = reverse("habits:habit_delete", args=[self.habit_2.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Habit.objects.count(), 3)
