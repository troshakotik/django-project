from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Имя пользователя", unique=True, max_length=150)
    email = models.EmailField("Электронная почта", unique=True)
    first_name = models.CharField("Имя", max_length=30, blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=30, blank=True, null=True)
    is_active = models.BooleanField("Активный", default=True)
    is_staff = models.BooleanField("Сотрудник", default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
