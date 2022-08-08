from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # What does this method do? If the method is our request is for reading then everybody has the access
    # but  if the method is not for reading only then only Admin can do something with it
    def has_permission(self, request, view):
        # Checking if the request is safe
        if request.method in permissions.SAFE_METHODS:
            return True  # If True we allow the access if False - not
        # Checking if the user is admin
        return bool(request.user and request.user.is_staff)

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # The same as in the class above
        if request.method in permissions.SAFE_METHODS:
            return True

        # If user from DB(obj.user) is the same as the user from request then he/she can update the data
        return obj.user == request.user


