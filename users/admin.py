from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )


admin.site.register(CustomUser, CustomUserAdmin)
