from django.contrib import admin

# Register your models here.
from Comments.models import CommentsModel


@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at', 'get_place_comment']
    list_display_links = ['author', 'created_at']
    list_per_page = 5

    @admin.display(description='Place comment')
    def get_place_comment(self, place: CommentsModel):
        """Метод для нахождения места комментария"""
        if place.lesson is not None and (place.assignment is None and place.submission is None):
            return f' Lesson - {place.lesson.name}'
        elif place.assignment is not None and (place.lesson is None and place.submission is None):
            return f'Assignment - {place.assignment.name}'
        else:
            return f'Submission - {place.submission.primary_key}'
