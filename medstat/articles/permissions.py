from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS  # это GET, OPTIONS и HEAD


class IsAuthenticated_CUSTOM(BasePermission):
    def has_permission(self, request, view):
        # ----------------------------
        # Накладываем условия!
        if request.user.is_authenticated:
        #----------------------------
            return True
        return False