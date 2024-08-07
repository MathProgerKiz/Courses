from rest_framework import permissions


class IsAdminJWTPerimission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Даем доступ только аутентифицированным пользователям
        if not request.user or not request.user.is_authenticated:
            return False



        if request.user.is_superuser and request.method == 'GET':
            return True
