from django.db.migrations import serializer
from rest_framework import serializers

from Assignments.models import AssignmentsModel


class AssignmentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=AssignmentsModel
        fields='__all__'
