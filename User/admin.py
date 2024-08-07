from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsersModel



admin.site.register(UsersModel, UserAdmin)
