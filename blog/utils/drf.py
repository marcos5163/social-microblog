from rest_framework import viewsets
from .exceptions import APITokenInvalidException, APITokenNotProvidedException
from social_blog import settings
from rest_framework.response import Response


class CustomAPIUtils:
    def error_response(self, status: int, data: dict = None, *args, **kwargs):
        final_data = data or {}
        assert isinstance(final_data, dict)
        response = {
            "status_code": status,
            "status": "failure",
            "data": final_data,
        }
        return Response(data=response, status=status)

    def success_response(self, status: int, data: dict = None, *args, **kwargs):
        final_data = data or {}
        assert isinstance(final_data, dict)
        response = {
            "status_code": status,
            "status": "success",
            "data": final_data,
        }
        return Response(data=response, status=status)


class BlogViewSet(viewsets.ViewSet, CustomAPIUtils):
    def check_permissions(self, request):
        api_token = request.META["autherization"]

        if not api_token:
            raise APITokenNotProvidedException

        if settings.CLIENT_API_TOKEN != api_token:
            raise APITokenInvalidException
