# Create your views here.
from rest_framework import viewsets

from Reviews.models import ReviewsModel
from Reviews.serializers import ReviewsSerializers


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializers

    def get_queryset(self):
        """Метод для получения записи урока по id из маршрута """
        lesson_id = self.kwargs.get('lesson__pk')
        if lesson_id:
            return ReviewsModel.objects.get(lesson_id=lesson_id)
        return ReviewsModel.objects.all()
