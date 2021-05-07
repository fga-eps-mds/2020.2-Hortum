from rest_framework import permissions

from ..users.models import User

class IsVerified(permissions.BasePermission):
    message = 'Email da conta não foi verificado'

    def has_permission(self, request, view):
        email = request.data['email']

        if not User.objects.filter(email=email).exists():
            return True

        user = User.objects.get(email=email)
        if user.is_verified:
            return True
        return False
