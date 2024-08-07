# Create your views here.
from rest_framework import viewsets

from Notifications.models import NotificationsModel
from Notifications.permissions import IsLector
from Notifications.serializers import NotificationSerializer
from User.models import UsersModel


class NotificationsViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsLector,)

    def get_queryset(self):
        """Метод для получения пользователя по id из маршрута"""
        user_id = self.kwargs.get('user__pk')
        if user_id:
            return NotificationsModel.objects.filter(user_id=user_id)
        return NotificationsModel.objects.all()
