from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .. import constants


def response_handler(role=constants.USER_ROLE):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if request.user and request.user.role != role:
                raise PermissionDenied(
                    detail="This user role does not have access to the API"
                )
            response, status = func(request, *args, **kwargs)
            return Response(response, status)

        return inner

    return decorator
