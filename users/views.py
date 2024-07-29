from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework import generics


class RegisterAPIView(generics.CreateAPIView):
    """Контроллер для регистрации нового пользователя"""

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     user.set_password(serializer.validated_data['password'])
    #     user.save()


class MyTokenObtainPairView(TokenObtainPairView):
    """Контроллер для получения JWT-токена"""

    serializer_class = MyTokenObtainPairSerializer
