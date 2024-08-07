

# Create your views here.
from rest_framework import viewsets

from Assignments.models import AssignmentsModel
from Assignments.permissions import IsLector
from Assignments.serializers import AssignmentsSerializers


class AssignmentsViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentsSerializers
    permission_classes = [IsLector]

    def get_queryset(self):
        """Метод для получения урока по id из маршрута"""
        queryset = AssignmentsModel.objects.all()
        lessons_id = self.kwargs.get('lessons__pk')
        if lessons_id:
            queryset = queryset.filter(lesson_id=lessons_id)
        return queryset
