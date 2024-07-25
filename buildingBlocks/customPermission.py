from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read-only actions (GET, HEAD, OPTIONS) for any request
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        # Write permissions are only allowed to admin users
        return request.user and request.user.is_authenticated and request.user.is_staff
