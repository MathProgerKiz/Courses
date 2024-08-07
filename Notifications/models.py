from django.db import models


from User.models import UsersModel


class NotificationsModel(models.Model):
    # Получатель уведомления (ссылка на модель User)
    recipient = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='notifications')
    # Сообщение уведомления
    message = models.TextField()
    # Прочитано или нет
    read = models.BooleanField(default=False, help_text="Отметьте, если уведомление было прочитано")
    # Дата создания уведомления
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата и время создания уведомления")

    objects = models.Manager()

    def __str__(self):
        return f"Notification for {self.recipient.name} "

    class Meta:
        verbose_name = 'Уведомления'
        verbose_name_plural = 'Уведомления'
