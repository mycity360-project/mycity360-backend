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
            page=request.query_params.get("page"),
            page_size=request.query_params.get("page_size"),
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
            phone=data.get("phone"),
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
