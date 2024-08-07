

# Create your views here.
from rest_framework import viewsets

from Submissions.permissions import IsStudent
from Submissions.models import SubmissionsModel
from Submissions.serializers import SubmissionsSerializers


class SubmissionsViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionsSerializers
    permission_classes = (IsStudent,)

    def get_queryset(self):
        """Метод для получения определенного задания по id"""
        queryset = SubmissionsModel.objects.all()
        assignments_id = self.kwargs.get('assignment__pk')

        if assignments_id:
            queryset = queryset.filter(assignment_id=assignments_id)
        return queryset
