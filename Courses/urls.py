
from django.urls import path, include
from rest_framework import routers

from Courses.views import CoursesViewSet

router=routers.DefaultRouter()
router.register(r'',CoursesViewSet)


urlpatterns = [
    # path('<int:pk>/', CoursesListAPIView.as_view()),
    # path('all/',CoursesViewSet.as_view({'get':'list'})),
    # path('create/',CoursesViewSet.as_view({'post':'create'})),
    # path('<int:pk>/',CoursesViewSet.as_view({'put':'update','delete':'destroy'})),
    # path('<int:pk>/', CoursesListAPIView.as_view())
    path('',include(router.urls))


]
