from rest_framework.permissions import SAFE_METHODS,BasePermission

class IsAuthenticated(BasePermission):
  def has_permission(self,request,view):
    return request.user.is_authenticated