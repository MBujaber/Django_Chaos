from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    message = "You must be the author of this recipes."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user
