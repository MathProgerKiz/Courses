from django.urls import path, include
from rest_framework_nested import routers
from .views import CommentViewSet
from Lessons.views import LessonsViewSet
from Assignments.views import AssignmentsViewSet
from Submissions.views import SubmissionsViewSet

router = routers.SimpleRouter()
router.register(r'lessons', LessonsViewSet, basename='lessons')
router.register(r'assignments', AssignmentsViewSet, basename='assignments')
router.register(r'submissions', SubmissionsViewSet, basename='submissions')

lessons_router = routers.NestedSimpleRouter(router, r'lessons', lookup='lesson')
lessons_router.register(r'comments', CommentViewSet, basename='lesson-comments')

assignments_router = routers.NestedSimpleRouter(router, r'assignments', lookup='assignment')
assignments_router.register(r'comments', CommentViewSet, basename='assignment-comments')

submissions_router = routers.NestedSimpleRouter(router, r'submissions', lookup='submission')
submissions_router.register(r'comments', CommentViewSet, basename='submission-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(lessons_router.urls)),
    path('', include(assignments_router.urls)),
    path('', include(submissions_router.urls)),
]
