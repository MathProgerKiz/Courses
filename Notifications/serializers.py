from rest_framework import serializers

from Notifications.models import NotificationsModel


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationsModel
        fields = '__all__'
