
from django.urls import path, include

from rest_framework_nested import routers

from Notifications.views import NotificationsViewSet

router = routers.SimpleRouter()
router.register(r'user', NotificationsViewSet, basename='user')

user_router = routers.NestedSimpleRouter(router, r'user', lookup='user')
user_router.register(r'notification', NotificationsViewSet, basename='user-notification')




urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(user_router.urls)),  # Вложенные маршруты

]
