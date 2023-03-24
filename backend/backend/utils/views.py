from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


def response_handler(role=None):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if (
                request.user.is_authenticated
                and role
                and request.user.role != role
            ):
                print(request.user.role)
                raise PermissionDenied(
                    detail="This user role does not have access to the API"
                )
            response, status = func(request, *args, **kwargs)
            return Response(response, status)

        return inner

    return decorator
