from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db.models import CharField, EmailField, BooleanField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator


class User(AbstractBaseUser, PermissionsMixin):
    phone_validator = RegexValidator(
        regex=r"^8\d{10}$", message="Допускается только российский номер телефона"
    )
    objects = UserManager()

    username = CharField(
        "Имя пользователя",
        unique=True,
        validators=[UnicodeUsernameValidator()],
        max_length=150,
    )
    is_staff = BooleanField("Сотрудник", default=False)
    is_active = BooleanField("Активен", default=True)
    phone_number = CharField(
        "Номер телефона", unique=True, validators=[phone_validator], max_length=20
    )
    email = EmailField("Электронная почта", unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("email", "phone_number")

    class Meta:
        verbose_name = "Пользователь"