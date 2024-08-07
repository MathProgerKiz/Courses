from django.urls import path, include
from rest_framework_nested import routers
from Assignments.views import AssignmentsViewSet
from Submissions.views import SubmissionsViewSet

router = routers.SimpleRouter()
router.register(r'assignments', AssignmentsViewSet, basename='assignments')

assignments_router = routers.NestedSimpleRouter(router, r'assignments', lookup='assignment')
assignments_router.register(r'submissions', SubmissionsViewSet, basename='assignment-submissions')
print(router.urls)
urlpatterns = [
    path('', include(router.urls)),  # Основные маршруты
    path('', include(assignments_router.urls)),  # Вложенные маршруты
]
