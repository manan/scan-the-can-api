from rest_framework import permissions


class IsCompany(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            comp = request.user.company
            print("is company")
            return True
        except Exception:
            print("is not company")
            return False
    
    def has_permission(self, request, view):
        try:
            comp = request.user.company
            print("is company")
            return True
        except Exception:
            print("is not company")
            return False

