<<<<<<< HEAD
from rest_framework import serializers
from habits.models import Place, Reward, Habit
from habits.validators import validate_habit


class PlaceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Место"""

    class Meta:
        model = Place
        fields = "__all__"


class RewardSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Вознаграждение"""

    class Meta:
        model = Reward
        fields = "__all__"


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и редактирования модели Привычка"""

    # фильтрация списка для поля reward_with_pleasing_habit: только привычки с признаком приятной привычки
    reward_with_pleasing_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.filter(is_pleasing_habit=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        return validate_habit(attrs)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Привычка"""

    class Meta:
        model = Habit
        fields = "__all__"
=======
from rest_framework import serializers
from habits.models import Place, Reward, Habit
from habits.validators import validate_habit


class PlaceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Место"""

    class Meta:
        model = Place
        fields = "__all__"


class RewardSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Вознаграждение"""

    class Meta:
        model = Reward
        fields = "__all__"


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и редактирования модели Привычка"""

    # фильтрация списка для поля reward_with_pleasing_habit: только привычки с признаком приятной привычки
    reward_with_pleasing_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.filter(is_pleasing_habit=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        return validate_habit(attrs)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Привычка"""

    class Meta:
        model = Habit
        fields = "__all__"
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
