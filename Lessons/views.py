from rest_framework import viewsets
from .models import LessonsModel
from .permissions import IsLector
from .serializers import LessonsSerializers


class LessonsViewSet(viewsets.ModelViewSet):
    serializer_class = LessonsSerializers
    permission_classes = IsLector,

    def get_queryset(self):
        """Метод для получения курса по id из маршрута"""
        queryset = LessonsModel.objects.all()
        course_id = self.kwargs.get('course__pk')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset
