from django.db import models
from User.models import UsersModel
from Assignments.models import AssignmentsModel


# Create your models here.
class SubmissionsModel(models.Model):
    student = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='submission')
    assignment = models.ForeignKey(AssignmentsModel, on_delete=models.CASCADE, related_name='submission')
    answer = models.CharField()  # Ответ на задание
    status = models.BooleanField(default=False)  # Статус проверено\не проверено) по умолчанию не проверено
    estimation = models.IntegerField()  # Оценка задания
    comment = models.TextField()  # комментарий преподавателя
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Ответы на задания'
        verbose_name_plural = 'Ответы на задания'
