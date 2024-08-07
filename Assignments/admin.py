from django.contrib import admin

# Register your models here.
from Assignments.models import AssignmentsModel


@admin.register(AssignmentsModel)
class AssignmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'due_date', 'lesson_id', 'get_lesson_order')
    list_display_links = ('name', 'due_date')
    ordering = ('lesson_id',)
    list_per_page = 5

    @admin.display(description='Порядок урока')
    def get_lesson_order(self, assignment: AssignmentsModel):
        return assignment.lesson.order
