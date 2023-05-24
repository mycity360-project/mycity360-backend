import traceback
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError, NotFound
from ..utils.google_api import send_mail


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
            try:
                response, status = func(request, *args, **kwargs)
            except ValidationError as e:
                raise e
            except NotFound as e:
                raise e
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                try:
                    send_mail(subject=f"{e}", body=str(e), to_email="heena4415@gmail.com, vibh1103@gmail.com")
                except:
                    print(traceback.format_exc())
                    print("Error in sending email")
                response = {"detail": str(e), "status_code": 500}
                status = 500
            return Response(response, status)

        return inner

    return decorator
