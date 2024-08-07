from django.urls import path, include
from rest_framework_nested import routers

from Lessons.views import LessonsViewSet

router = routers.SimpleRouter()
router.register(r'courses', LessonsViewSet, basename='courses')

courses_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
courses_router.register(r'lessons', LessonsViewSet, basename='courses-lessons')

urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(courses_router.urls)),  # Вложенные маршруты
]
