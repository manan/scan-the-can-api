from rest_framework import permissions


class IsUserOfProfile(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    
    def has_permission(self, request, view):
        user_id = request.user.id
        company_user_id = request.data['user']
        if company_user_id is not None:
            return company_user_id == user_id
        return False
