from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import DateTimeField

class User(AbstractBaseUser, PermissionsMixin):
    pass
