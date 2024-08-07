from django.db import models

from Courses.models import CoursesModel
from User.models import UsersModel


class ReviewsModel(models.Model):
    # Уникальный идентификатор для отзыва

    # Курс, к которому относится отзыв (ссылка на модель Course)
    course = models.ForeignKey(CoursesModel, on_delete=models.CASCADE, related_name='reviews')
    # Студент, оставивший отзыв (ссылка на модель User)
    student = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='reviews')
    # Рейтинг отзыва
    rating = models.IntegerField(help_text="Рейтинг курса от 1 до 5")
    # Содержание отзыва
    review_text = models.TextField(help_text="Текст отзыва о курсе")
    # Дата создания отзыва
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания отзыва")

    objects = models.Manager()

    def __str__(self):
        return f"Review by {self.student.username} for {self.course.name} "

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

