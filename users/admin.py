from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CutstomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CutstomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "phone_number", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
