
from django.urls import path, include

from rest_framework_nested import routers

from Assignments.views import AssignmentsViewSet

router = routers.SimpleRouter()
router.register(r'lessons', AssignmentsViewSet, basename='assignments')

lessons_router = routers.NestedSimpleRouter(router, r'lessons', lookup='lesson')
lessons_router.register(r'assignments', AssignmentsViewSet, basename='lesson-assignments')



print(router.urls)
urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(lessons_router.urls)),  # Вложенные маршруты

]
