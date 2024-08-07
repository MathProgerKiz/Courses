from rest_framework import serializers

from Lessons.models import LessonsModel


class LessonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LessonsModel
        fields = '__all__'
