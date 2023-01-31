from rest_framework import permissions
from pprint import pprint

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        #eğer permissions safe methodu içerisindeyse(get,head,options) true dön 
        #değilse de is_admin olup olmadığına bak
        return request.method in permissions.SAFE_METHODS or is_admin

class IsCommentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.comment_owner #false gelirse başka kullanıcının yorumuna müdahale edemez sadece görebilir