from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models import CharField
from django.contrib.auth.validators import UnicodeUsernameValidator

class User(AbstractBaseUser, PermissionsMixin):
    username = CharField("Имя пользователя", unique=True, validators=[UnicodeUsernameValidator()], max_length=150)
    USERNAME_FIELD = "username"