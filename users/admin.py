<<<<<<< HEAD
from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "is_active",
        "chat_id",
    )


admin.site.register(User, UserAdmin)
=======
from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "is_active",
        "chat_id",
    )


admin.site.register(User, UserAdmin)
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
