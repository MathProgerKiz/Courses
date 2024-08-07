from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Даем доступ только аутентифицированным пользователям
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли текущий пользователь автором объекта
        # или обладает ли он правами суперпользователя (админа)
        return obj.author == request.user or request.user.is_superuser

