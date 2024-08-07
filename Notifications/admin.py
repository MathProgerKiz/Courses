from django.contrib import admin

# Register your models here.
from Notifications.models import NotificationsModel


@admin.register(NotificationsModel)
class NotificationAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['recipient_id', 'read', 'created_at']
    list_display_links = ['recipient_id', 'read', 'created_at']
