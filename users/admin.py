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
