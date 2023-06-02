from rest_framework import permissions

class IsCoworkerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.is_coworker and request.user.is_coworker is True