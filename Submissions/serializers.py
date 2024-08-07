from rest_framework import serializers

from Submissions.models import SubmissionsModel


class SubmissionsSerializers(serializers.ModelSerializer):
    class Meta:
        model=SubmissionsModel
        fields='__all__'
