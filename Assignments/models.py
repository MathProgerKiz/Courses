from django.db import models
from Lessons.models import LessonsModel


# Create your models here.
class AssignmentsModel(models.Model):
    name = models.CharField()
    description = models.TextField()
    lesson = models.ForeignKey(LessonsModel, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateTimeField(help_text="Дата и время, к которым должно быть сдано задание")  # Дата сдачи задания

    objects = models.Manager()

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'{self.name}'
