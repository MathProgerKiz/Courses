from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import CommentsModel
from .permissions import IsAuthorOrAdmin
from .serializers import CommentSerializer


class CommentViewSet(CreateModelMixin,
                     DestroyModelMixin,
                     ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["lesson__id", 'assignment__id', 'submission__id']

    def get_queryset(self):
        """В данном методе выбирается одна запись в зависимости от какой сущности достается комментарии"""
        queryset = CommentsModel.objects.all()
        lesson_id = self.kwargs.get('lesson__pk')
        assignment_id = self.kwargs.get('assignment__pk')
        submission_id = self.kwargs.get('submission__pk')

        if lesson_id:
            queryset = queryset.filter(lesson_id=lesson_id)
        elif assignment_id:
            queryset = queryset.filter(assignment_id=assignment_id)
        elif submission_id:
            queryset = queryset.filter(submission_id=submission_id)

        return queryset

    def perform_destroy(self, instance):
        """Данный метод при попытке удалить комментарии проверяет
           является ли данный пользователь владельцем комментария
        """
        if instance.author != self.request.user:
            raise PermissionDenied("Вы не являетесь автором этого комментария.")
        instance.delete()
