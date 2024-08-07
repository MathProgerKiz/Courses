from rest_framework import permissions


class IsLector(permissions.BasePermission):
    def has_permission(self, request, view):
        # Даем доступ только аутентифицированным пользователям
        if not request.user or not request.user.is_authenticated:
            return False

        # Разрешаем доступ к методам GET всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешаем доступ только преподавателям для методов POST, PUT, DELETE

        return request.user.role == 'lector'
