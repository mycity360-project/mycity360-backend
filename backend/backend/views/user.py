from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from ..controllers import user as user_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler(ADMIN_ROLE)
def user_list(request):
    if request.method == "GET":
        response = user_controller.list_user(
            is_active=request.query_params.get("is_active"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 10),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = user_controller.create_user(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT"])
@response_handler()
def user_details(request, pk):
    if request.method == "GET":
        response = user_controller.get_user(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = user_controller.update_user(pk, request.data)
        return response, status.HTTP_200_OK


@api_view(["GET", "PUT", "DELETE"])
@response_handler(ADMIN_ROLE)
def user_details_admin(request, pk):
    if request.method == "GET":
        response = user_controller.get_user(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = user_controller.update_user(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = user_controller.delete_user(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def signup(request):
    if request.method == "POST":
        response = user_controller.signup(**request.data)
        return response, status.HTTP_201_CREATED


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def login(request):
    if request.method == "POST":
        data = request.data
        headers = request.headers
        response = user_controller.login(
            email=data.get("email"),
            password=data.get("password"),
            client_id=headers.get("Clientid"),
        )
        return response, status.HTTP_201_CREATED


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def verify_otp(request, pk):
    if request.method == "POST":
        data = request.data
        headers = request.headers
        response = user_controller.verify_otp(
            pk=pk,
            email_otp=data.get("email_otp"),
            phone_otp=data.get("phone_otp"),
            client_id=headers.get("Clientid"),
        )
        return response, status.HTTP_201_CREATED


@api_view(["POST"])
@response_handler()
def user_image_upload(request, pk):
    response = user_controller.upload_profile_image(
        pk, request.FILES.get("file")
    )
    return response, status.HTTP_200_OK


@api_view(["POST"])
@response_handler()
def change_password(request, pk):
    response = user_controller.change_password(
        pk,
        new_password=request.data.get("new_password"),
        current_password=request.data.get("current_password"),
    )
    return response, status.HTTP_200_OK


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def forgot_password(request):
    response = user_controller.forgot_password(
        key=request.data.get("key"),
    )
    return response, status.HTTP_200_OK


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def reset_password(request):
    response = user_controller.reset_password(
        otp=request.data.get("otp"),
        password=request.data.get("password"),
        email=request.data.get("email"),
        phone=request.data.get("phone"),
    )
    return response, status.HTTP_200_OK


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def resend_otp(request, pk):
    response = user_controller.resend_otp(
        pk=pk,
    )
    return response, status.HTTP_200_OK
