from rest_framework import viewsets

from Courses.models import CoursesModel
from Courses.permissions import IsLector

from Courses.serializers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsLector]



