from rest_framework.permissions import BasePermission

class NoDownloadPermission(BasePermission):
    message = 'You are not allowed to download videos.'

    def has_permission(self, request, view):
        return not request.method == 'GET' or 'download' not in request.query_params