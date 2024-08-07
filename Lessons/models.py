from django.db import models
from Courses.models import CoursesModel


# Create your models here.
class LessonsModel(models.Model):
    name = models.CharField()
    description = models.TextField()
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='lesson')
    materials = models.CharField()  # материал (ссылки на видео/ресурсы )
    order = models.CharField()  # поле Порядок: Используется для упорядочивания уроков внутри курса,определяя последовательность

    objects = models.Manager()

    class Meta:
        verbose_name = 'Уроки'
        verbose_name_plural = 'Уроки'
