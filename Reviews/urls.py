from django.urls import path, include
from rest_framework_nested import routers
from Assignments.views import AssignmentsViewSet
from Reviews.views import ReviewsViewSet
from Submissions.views import SubmissionsViewSet

router = routers.SimpleRouter()
router.register(r'course', ReviewsViewSet, basename='course')

course_router = routers.NestedSimpleRouter(router, r'course', lookup='course')
course_router.register(r'reviews', ReviewsViewSet, basename='assignment-submissions')

urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(course_router.urls)),  # Вложенные маршруты
]
