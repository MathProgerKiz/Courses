from django.contrib import admin

# Register your models here.
from Courses.models import CoursesModel


@admin.register(CoursesModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'get_lector']
    list_display_links = ['name', 'date', ]
    list_per_page = 5

    @admin.display(description='lector')
    def get_lector(self, course: CoursesModel):
        return course.lector.username
