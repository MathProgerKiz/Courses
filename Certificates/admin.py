from django.contrib import admin

# Register your models here.
from Certificates.models import CertificatesModel


@admin.register(CertificatesModel)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'issue_date', 'status']
    list_display_links = ['student', 'course', 'issue_date', 'status']
    list_per_page = 5
