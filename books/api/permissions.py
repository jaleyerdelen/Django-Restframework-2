from rest_framework import permissions
from pprint import pprint

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        #eğer permissions safe methodu içerisindeyse(get,head,options) true dön 
        #değilse de is_admin olup olmadığına bak
        return request.method in permissions.SAFE_METHODS or is_admin

