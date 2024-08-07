from django.db import models
from User.models import UsersModel


# Create your models here.

class CoursesModel(models.Model):
    name = models.CharField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Дата создания курса
    lector = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='course')  # Преподаватель

    objects = models.Manager()

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.name}'
