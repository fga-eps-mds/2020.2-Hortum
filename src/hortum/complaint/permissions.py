from rest_framework import permissions

from ..customer.models import Customer

class IsCustomer(permissions.BasePermission):
    message = 'Usuário não é um consumidor.'

    def has_permission(self, request, view):
        return Customer.objects.filter(user__email=request.user).exists()