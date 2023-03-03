from rest_framework.response import Response


def response_handler():
    def decorator(func):
        def inner(request, *args, **kwargs):
            response, status = func(request, *args, **kwargs)
            return Response(response, status)

        return inner

    return decorator
