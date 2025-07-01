from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "username")


admin.site.register(CustomUser, CustomUserAdmin)
