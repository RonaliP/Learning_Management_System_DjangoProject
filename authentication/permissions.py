from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Admin'

class IsMentor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Admin' or request.user.role == 'Mentor':
            return True
        else:
            return False