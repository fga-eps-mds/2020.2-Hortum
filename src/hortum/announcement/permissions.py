from rest_framework import permissions

from .models import Productor

class IsProductor(permissions.BasePermission):
    message = 'Usuário não é um produtor.'

    def has_permission(self, request, view):
        return Productor.objects.filter(user__email=request.user).exists()

class IsOwnerAnnouncement(permissions.BasePermission):
    message = 'Anúncio não pertence ao usuário.'

    def has_permission(self, request, view):
        productor = Productor.objects.get(user__email=request.user)
        return productor.announcements.filter(name=view.kwargs['name']).exists()