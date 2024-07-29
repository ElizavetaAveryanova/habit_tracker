<<<<<<< HEAD
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    PlaceViewSet,
    RewardViewSet,
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    PublicHabitListAPIView,
)
from rest_framework.routers import DefaultRouter

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"place", PlaceViewSet, basename="place")
router.register(r"reward", RewardViewSet, basename="reward")


urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("public_habit/", PublicHabitListAPIView.as_view(), name="public_habit_list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_get"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
] + router.urls
=======
from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    PlaceViewSet,
    RewardViewSet,
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    PublicHabitListAPIView,
)
from rest_framework.routers import DefaultRouter

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"place", PlaceViewSet, basename="place")
router.register(r"reward", RewardViewSet, basename="reward")


urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit_list"),
    path("public_habit/", PublicHabitListAPIView.as_view(), name="public_habit_list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_get"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
] + router.urls
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
