from rest_framework import permissions
from datetime import datetime

class OwnerAccessPermission(permissions.BasePermission):
    message = 'You are not allowed to access, you not the owner or an admin'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        else:
            return False


class ModificationPermission(permissions.BasePermission):
    message = "Days allowed to updated or cancel a booking have expired"

    def has_object_permission(self, request, view, obj):
        if (obj.date - datetime.now().date()).days > 3:
            return True
        else:
            return False
