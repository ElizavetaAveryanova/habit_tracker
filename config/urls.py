from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)