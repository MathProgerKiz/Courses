from django.contrib import admin

# Register your models here.
from Submissions.models import SubmissionsModel


@admin.register(SubmissionsModel)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'assignment_id', 'status', 'estimation', 'date']
    list_display_links = ['student_id', 'assignment_id', 'status', 'estimation', 'date']
    list_per_page = 5



