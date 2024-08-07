from rest_framework import serializers

from Courses.models import CoursesModel


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoursesModel
        fields = '__all__'