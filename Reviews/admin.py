from django.contrib import admin

# Register your models here.
from Reviews.models import ReviewsModel


@admin.register(ReviewsModel)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'student_id', 'rating', 'created_at']
    list_display_links = ['course_id', 'student_id', 'rating', 'created_at']
    list_per_page = 5
