from datetime import timezone

from django.db import models

# Create your models here.
from User.models import UsersModel
from Courses.models import CoursesModel
from django.utils import timezone


class CertificatesModel(models.Model):
    student = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='certificate')
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='certificate')
    issue_date = models.DateTimeField(default=timezone.now, help_text="Дата и время, когда был выдан сертификат")
    status = models.BooleanField(default=False)  # выдан/не выдан  сертификат по умочанию не выдан

    objects = models.Manager()

    class Meta:
        verbose_name = 'Сертификаты'
        verbose_name_plural = 'Сертификаты'
