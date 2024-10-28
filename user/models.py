from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class BaseUserManager(BaseUserManager):
    '''Базовый класс для создания юзеров и суперюзеров'''

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have a username.")
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")

        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Кастомная модель юзера'''

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = BaseUserManager()

    def __str__(self):
        return self.username
