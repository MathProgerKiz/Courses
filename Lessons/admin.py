from django.contrib import admin

# Register your model
from Lessons.models import LessonsModel

@admin.register(LessonsModel)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id', 'order']
    list_display_links = ['name', 'course_id', 'order']
    list_per_page = 5

