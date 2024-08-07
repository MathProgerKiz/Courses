from rest_framework import serializers

from Reviews.models import ReviewsModel


class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=ReviewsModel
        fields='__all__'