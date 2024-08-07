


from django.db import models


from Assignments.models import AssignmentsModel
from Lessons.models import LessonsModel
from Submissions.models import SubmissionsModel
from User.models import UsersModel


class CommentsModel(models.Model):
    # Уникальный идентификатор для комментария

    # Автор комментария (ссылка на модель User)
    author = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    # Содержание комментария
    content = models.TextField()
    # Дата создания комментария
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания комментария")
    # Урок, к которому относится комментарий (необязательно)
    lesson = models.ForeignKey(LessonsModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    # Задание, к которому относится комментарий (необязательно)
    assignment = models.ForeignKey(AssignmentsModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    # Ответ, к которому относится комментарий (необязательно)
    submission = models.ForeignKey(SubmissionsModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')

    objects = models.Manager()

    def __str__(self):
        return f"Comment by {self.author.username} "

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
