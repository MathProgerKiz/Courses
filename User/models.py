
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.

class UsersModel(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30)  # Тип пользователя (студент, преподаватель, администратор)
    date = models.DateTimeField(auto_now_add=True)  # Дата регистрации

    objects = UserManager()



    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


