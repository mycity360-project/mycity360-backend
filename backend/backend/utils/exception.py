from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        # response.data['status_code'] = response.status_code
        data = response.data
        response.data = {
            # "detail": response.data,
            "status_code": response.status_code,
        }
        if type(data) == list:
            response.data["detail"] = data[0]
        elif data.get("detail"):
            response.data["detail"] = data.get("detail")
        else:
            response.data["detail"] = data

    return response
