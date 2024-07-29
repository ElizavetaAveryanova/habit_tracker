<<<<<<< HEAD
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterAPIView, MyTokenObtainPairView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
=======
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterAPIView, MyTokenObtainPairView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
